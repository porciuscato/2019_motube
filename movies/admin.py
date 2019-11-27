from django.contrib import admin
from .models import Movie, Genre, Review, Video, Movie_Score

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Video)
admin.site.register(Movie_Score)