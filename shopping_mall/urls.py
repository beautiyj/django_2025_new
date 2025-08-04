from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_shopping_mall),  #한줄추가
]