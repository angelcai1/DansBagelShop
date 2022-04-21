from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateOrder

#TODO you can change the name of this view to something else other than orders, up to you
def orders(request):   
    return render(request, 'orders/orders.html')