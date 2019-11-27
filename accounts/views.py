from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from movies.models import Review
from IPython import embed

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
    reviews = Review.objects.filter(author=user_pk)
    context = {
        'person': person,
        'reviews': reviews,
        'like_movies': like_movies,
    }
    return render(request, 'accounts/detail.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index') 
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
