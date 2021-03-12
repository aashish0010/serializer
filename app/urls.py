from django.urls import path, include
from . import views

urlpatterns = [
    path('home/<int:pk>',views.home),
    path('',views.all)
    ]