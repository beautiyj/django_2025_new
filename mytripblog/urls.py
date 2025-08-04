from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #한줄추가
]