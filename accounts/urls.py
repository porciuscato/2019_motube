from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_pk>/', views.user_detail, name="user_detail"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name="delete"),
]
