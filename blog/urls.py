from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),  # 상세페이지 뷰 (FBV)
    path('', views.index, name='index'),             # 리스트 페이지 뷰 (FBV)
]
