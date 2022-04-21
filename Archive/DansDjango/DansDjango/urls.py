from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    # register urls from accounts app
    #path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('orders/',include('orders.urls')),
    path('', views.homepage),
]

#urlpatterns += staticfiles_urlpatterns