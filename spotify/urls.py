from django.urls import path, include
from . import views

urlpatterns = [
    path('get-auth-url', views.AuthURL.as_view()),
    path('redirect', views.spotify_callback),
    path('is-authenticated', views.IsAutenticated.as_view()),
    path('current-song', views.CurrentSong.as_view()),
    path('pause/', views.PlaySong.as_view()),
    path('play/', views.PauseSong.as_view()),
    path('skip/', views.SkipSong.as_view()),
]
