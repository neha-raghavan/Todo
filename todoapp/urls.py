from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('createTask/', views.createTask,name='createTask'),
    path('delete_task/<str:pk>/', views.DeleteTask,name='delete_task'),
    path('update_task/<str:pk>/', views.UpdateTask,name='update_task'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('reset_password/', views.user_login,name='reset_password'),
    
]
