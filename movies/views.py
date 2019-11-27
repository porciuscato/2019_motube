from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
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

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'movies/detail.html', context)

def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if user.like_movies.filter(pk=movie_pk).exists():
        user.like_movies.remove(movie)
    else:
        user.like_movies.add(movie)
    return redirect("movies:index")

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
