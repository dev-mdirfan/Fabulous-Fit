from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:pk>/', views.post, name='post'),
]