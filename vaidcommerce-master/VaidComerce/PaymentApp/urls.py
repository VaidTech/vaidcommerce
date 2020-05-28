from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('payment/<int:id>/', views.get_payment, name="payment"),
       
    
]