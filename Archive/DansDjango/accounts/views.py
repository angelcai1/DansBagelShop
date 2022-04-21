from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
            #If valid then save it to the database
        if form.is_valid():
            form.save()
            #log user in
            return redirect('index.html')
    #If it's a GET request
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form':form})

def login_page(request):
    if request.method == "POST":
        #sending the data into this form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Login the user if it is avlid
            return redirect('orders:')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})


# def signup_page(request):
#     context = {}
#     form = UserCreationForm(request.POST or None)
#     if request.method == "POST":
#         #If valid then save it to the database
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return render(request,'accounts/index.html')
#     context['form']=form
#     return render(request,'registration/sign_up.html',context)
#     #Create a new instance of the form and store it in variable 'form'
#     form = UserCreationForm()
#     #Send that form to the template
#     return render(request, 'accounts/signup.html', {'form':form})

#@login_required
#def index(request):
#    return render(request,'accounts/index.html')
