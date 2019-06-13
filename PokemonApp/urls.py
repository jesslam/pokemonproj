from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getpokemon/', views.getpokemon, name='pokemon'),
    path('pokemondetail/<int:id>', views.pokemondetail, name='pokemondetail'),
    path('getevaluation/', views.getevaluation, name='evaluation'),
    path('neweval/', views.newEvaluation, name='neweval'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]