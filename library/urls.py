from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_library),  #한줄추가
]