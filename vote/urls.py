from django.contrib import admin
from django.urls import path
from vote import views

urlpatterns = [
    path('', views.voteEmpty, name='voteEmpty'),
    path('vote/', views.vote, name='vote'),
    path('finished/', views.finished, name='finished')
]
