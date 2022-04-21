from django.contrib import admin
from django.urls import path,include
from .import views

app_name='orders'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('', views.active_orders,name="Active orders"),

]
