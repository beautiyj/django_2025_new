from django.urls import path
from . import views
urlpatterns=[
    path('category/<slug>/',views.category,name='category'),
    path('', views.index , name='index'),
    path('<int:pk>/', views.detail, name='detail' ),
    path('create/', views.create , name='blogcreate'),
    path('<int:pk>/delete/', views.delete , name='blogdelete'),
    path('<int:pk>/update/', views.update , name='blogupdate'),
    #path('<int:pk>/comment/', views.comment , name='blogcomment'),
    path('<int:pk>/createcomment/', views.createcomment, name='blogcreatecomment'),
    path('<int:pk>/updatecomment/', views.updatecomment, name='blogupdatecomment'),
    path('<int:pk>/deletecomment/', views.deletecomment, name='blogdeletecomment'),
]