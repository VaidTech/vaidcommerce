
from django.contrib import admin
from django.urls import path
from.import views
 

urlpatterns = [
    path('', views.get_index, name="index"),
    path('login/', views.get_login, name="login"),
    path('logout/', views.get_logout, name="logout"),
    path('register/', views.get_register, name="register"),
    path('activate/<uidb64>/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/', views.get_activate, name="activate"),
    path('verify/', views.get_verify, name="verify"),
     
     
        
]
 

