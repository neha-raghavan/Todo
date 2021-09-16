from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('createTask/', views.createTask,name='createTask'),
    path('delete_task/<str:pk>/', views.DeleteTask,name='delete_task'),
    path('update_task/<str:pk>/', views.UpdateTask,name='update_task'),
    
]
