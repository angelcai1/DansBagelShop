from django.shortcuts import render

# Create your views here.
def active_orders(request):
    return render(request, 'orders/active_orders.html')
