from django.urls import path
from . import views


urlpatterns=[
    path('<int:animation_pk>/article/', views.article),
    path('<int:animation_pk>/article/<int:article_pk>/like/', views.like),
    path('<int:animation_pk>/article/<int:article_pk>/comment/', views.comment),
]