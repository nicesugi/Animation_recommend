from django.urls import path
from . import views


urlpatterns=[

    path('signup/', views.sign_up),
    path('login/', views.view_login),
    path('<str:username>/follow/', views.follow),
    path('view_follow/', views.view_follow),
    path('view_like/', views.view_like),


]