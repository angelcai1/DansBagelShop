from django.shortcuts import render, redirect

# Create your views here.
def home_screen_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    context['user'] = request.user
    return render(request, 'screens/home.html', context)
