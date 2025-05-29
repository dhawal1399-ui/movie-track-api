from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register_user, name='register'),
    path('movies/', views.movie_list_create, name='movie-list-create'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),
]
