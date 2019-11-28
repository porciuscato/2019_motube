from django.db import models
from django.conf import settings
from django_pandas.managers import DataFrameManager

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    open_date = models.CharField(max_length=20)
    description = models.TextField()
    audi_score = models.IntegerField()
    net_score = models.IntegerField()
    press_score = models.IntegerField()
    audi = models.IntegerField()
    rate = models.CharField(max_length=20)
    naver_code = models.CharField(max_length=20)
    poster = models.TextField()
    youtube_score = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", blank=True)
    genre = models.ManyToManyField(Genre, related_name="genre_movies")
    watched_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watched_movie", blank=True)

    class Meta:
        ordering = ('-youtube_score', )

    def __str__(self):
        return self.title

class Video(models.Model):
    channelId = models.CharField(max_length=50)
    channelTitle = models.CharField(max_length=100)
    videoTitle = models.CharField(max_length=100)
    description = models.TextField()
    videoId = models.CharField(max_length=50)
    created_at = models.CharField(max_length=100)
    thumbnail_small = models.CharField(max_length=200)
    thumbnail_medium = models.CharField(max_length=200)
    thumbnail_high = models.CharField(max_length=200)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    comment_count = models.IntegerField()
    video_src = models.CharField(max_length=200)
    iframe = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.videoTitle

class Review(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.content

class Movie_Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.FloatField()
    
    objects = DataFrameManager()