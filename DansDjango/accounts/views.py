from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, PasswordUpdateForm, BalanceUpdateForm
from django.contrib.auth import login, authenticate, logout


def sign_up(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form
    return render(request, 'accounts/login.html', context)


def settings_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, "accounts/settings.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        accountForm = AccountUpdateForm(request.POST, instance = request.user)
        if accountForm.is_valid():
            accountForm.initial = {
                "email" : request.POST['email'],
                "username" : request.POST['username'],
                "first_name" : request.POST['first_name'],
                "last_name" : request.POST['last_name'],
                "phone" : request.POST['phone'],
                "address" : request.POST['address'],
                "city" : request.POST['city'],
                "state" : request.POST['state'],
                "zipcode" : request.POST['zipcode'],
            }
            accountForm.save()
            context['account_success_message'] = "Updated User"
        
    else:
        accountForm = AccountUpdateForm(
            initial = {
                "email" : request.user.email,
                "username" : request.user.username,
                "first_name" : request.user.first_name,
                "last_name" : request.user.last_name,
                "phone" : request.user.phone,
                "address" : request.user.address,
                "city" : request.user.city,
                "state" : request.user.state,
                "zipcode" : request.user.zipcode,
            }
        )
    context['account_form'] = accountForm        
    return render(request, 'accounts/account.html', context)


def password_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:        
        passwordForm = PasswordUpdateForm(request.POST, instance = request.user)
        if passwordForm.is_valid():
            passwordForm.initial = {
                "password" : request.POST['password1'],
            }
            passwordForm.save()
            context['password_success_message'] = "Updated Password"
    else:
        passwordForm = PasswordUpdateForm()      
    context['password_form'] = passwordForm
    return render(request, 'accounts/password.html', context)


def balance_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        balanceForm = BalanceUpdateForm(request.POST, instance = request.user)
        if balanceForm.is_valid():
            balanceForm.initial = {
                "balance" : request.POST['balance'],
            }
            balanceForm.save()
            context['balance_success_message'] = "Updated Balance"
        
    else:
        balanceForm = BalanceUpdateForm(
            initial = {
                "balance" : request.user.balance,
            }
        )
    context['balance_form'] = balanceForm
    return render(request, 'accounts/balance.html', context)