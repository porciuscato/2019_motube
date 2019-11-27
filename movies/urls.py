from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/review/', views.create_review, name="create_review"),
    path('<int:movie_pk>/review/delete/<int:review_pk>/', views.delete_review, name="delete_review"),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:movie_pk>/score/', views.create_score, name='create_score'),
]