from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', views.detail, name='detail'),
]
