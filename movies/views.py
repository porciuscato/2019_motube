from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Video, Movie_Score
from .forms import ReviewForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from IPython import embed

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    videos = Video.objects.filter(movie=movie_pk)
    videos = [ele for ele in videos]
    video_srcs = [ele.video_src for ele in videos]
    first_src = video_srcs[0]
    rem_src = video_srcs[1:5]
    # 좋아요한 목록을 보자...
    rated_movie = Movie_Score.objects.filter(user=request.user, movie=movie)
    if rated_movie:
        rated = rated_movie[0].score
    else:
        rated = False
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
        'videos': videos,
        'first_src': first_src,
        'rem_src': rem_src,
        'rated': rated,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if user.like_movies.filter(pk=movie_pk).exists():
        user.like_movies.remove(movie)
        liked = False
    else:
        user.like_movies.add(movie)
        liked = True
    like_users = list(movie.like_users.all().values())
    context = {
        'liked': liked,
    }
    return JsonResponse(context)

@login_required
def delete_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)

@login_required
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
    return redirect("movies:detail", movie_pk)

@login_required
def create_score(request, movie_pk, score):
    movie_score = Movie_Score.objects.filter(user=request.user.pk, movie=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie_score.exists():
        target = movie_score[0]
        target.score = score
        target.save()
    else:
        instance = Movie_Score(user=request.user, movie=movie, score=score)
        instance.save()
    return redirect('movies:detail', movie_pk)

@login_required
def search(request):
    q = request.GET.get('query', '')
    result = []
    if q:
        result += Movie.objects.filter(title__icontains=q)
    if not result:
        result = False
    context = {
        'q': q,
        'result': result
    }
    return render(request, 'movies/search.html', context)