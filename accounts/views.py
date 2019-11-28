import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from movies.models import Movie, Movie_Score
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from movies.models import Review
from IPython import embed
from django_pandas.io import read_frame
import math

def sim_pearson(data, name1, name2):
    sumX=0 # X의 합
    sumY=0 # Y의 합
    sumPowX=0 # X 제곱의 합
    sumPowY=0 # Y 제곱의 합
    sumXY=0 # X*Y의 합
    count=0 #영화 개수
    if not data.get(name1):
        return 0
    for i in data[name1]: # i = key
        if math.isnan(data[name1][i]):
            continue
        if math.isnan(data[name2][i]):
            continue
        # name1, name2 둘 다 관심있는 영화
        sumX+=data[name1][i]
        sumY+=data[name2][i]
        sumPowX+=pow(data[name1][i],2)
        sumPowY+=pow(data[name2][i],2)
        sumXY+=data[name1][i]*data[name2][i]
        count+=1
    
    if count == 0:
        return 0
    a = sumXY- ((sumX*sumY)/count)
    b = (sumPowX - (pow(sumX,2) / count))
    c = (sumPowY - (pow(sumY,2) / count))
    d = math.sqrt(b * c)
    if d == 0:
        return 0
    return a / d

def top_match(data, name, index=3):
    li=[]
    for i in data: #딕셔너리를 돌고
        if name!=i: #자기 자신이 아닐때만
            li.append((sim_pearson(data,name,i),i)) #sim_function()을 통해 상관계수를 구하고 li[]에 추가
    li.sort() #오름차순
    li.reverse() #내림차순
    return li[:index]

def get_recommend(data, person):
    if not data.get(person):
        return []
    res = top_match(data, person)
    if not res:
        return []
    sim_person = max(res)[1]
    lst = []
    for movie in data[sim_person]:
        if math.isnan(data[sim_person][movie]):
            continue
        if math.isnan(data[person][movie]):
            lst.append(movie)

    return lst[:4]

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context=context)

def user_detail(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    like_movies = person.like_movies.all()
    scores = Movie_Score.objects.all()
    if scores:
        ratings = scores.to_pivot_table(values='score', rows='movie', cols='user').to_dict()
        movie_names = get_recommend(ratings, request.user.username)
        movie_lst = []
        for name in movie_names:
            movie = Movie.objects.filter(title=name)[0]
            movie_lst.append(movie)
    else:
        movie_lst = []
    context = {
        'person': person,
        'like_movies': like_movies,
        "reco_movies": movie_lst
    }
    return render(request, 'accounts/detail.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
        return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/form.html', context=context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/form.html', context=context)


@login_required
def delete(request):
    request.user.delete()
    return redirect("accounts:signup")

@login_required
def follow(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)

    return redirect("accounts:user_detail", person_pk)
