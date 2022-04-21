from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from .import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup_page, name="signup"),
    path('login/', views.login_page, name="login"),
    path('', include('accounts.urls')),
    path('accounts/', include("django.contrib.auth.urls")),

]
