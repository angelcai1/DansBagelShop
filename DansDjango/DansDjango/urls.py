from django.contrib import admin
from django.urls import include, path

from accounts.views import (
    sign_up,
    logout_view,
    login_view,
    account_view,
    settings_view,
    password_view,
    balance_view,
)

from screens.views import (
    home_screen_view,
)
from menu.views import menu, inventory
from orders.views import orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login"),
    path('register/', sign_up, name="register"),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name="login"),
    path('home/', home_screen_view, name='home'),
    path('settings/', settings_view, name='settings'),
    path('settings/account/', account_view, name='account'),
    path('settings/password/', password_view, name='password'),
    path('settings/balance/', balance_view, name='balance'),
    #path('home/menu', menu, name='menu'),
    path('home/orders', orders, name='orders'),
    #path('home/inventory', inventory, name='inventory'),
    path('home/', include(('menu.urls'),namespace="menu_app")),
    
    path('orders/', include(('orders.urls'),namespace="orders_app")),
    #path('home/inventory', include(('menu.urls'),namespace="menu_app")),
]

