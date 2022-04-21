from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/sign_up/', views.sign_up, name="sign_up"),
]
