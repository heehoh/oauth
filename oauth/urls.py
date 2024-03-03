from django.http import HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('oauth/', views.index),
]