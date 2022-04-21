from django.urls import path
from . import views

app_name = "orders_app"
urlpatterns = [
    path('orders/', views.orders, name = 'orders'),

]
