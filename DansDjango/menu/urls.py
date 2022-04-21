from django.urls import path
from . import views

app_name = "menu_app"
urlpatterns = [
    path('menu/', views.menu, name = 'menu'),
    path('inventory/', views.inventory, name = 'inventory'),
]
