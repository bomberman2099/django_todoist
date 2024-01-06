from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse


def UserRegisterView(request):
    if request.user.is_authenticated:
        redirect(reverse("home_app:home"))
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('Email')
            password = form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            form.save()
            return redirect(reverse('home_app:home'))

    else:

        form = UserRegisterForm()

    return render(request, 'user_app/UserRegister.html', {'form': form})

def UserLoginView(request):
    if request.user.is_authenticated:
        redirect(reverse("home_app:home"))
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                form.save()
                return redirect(reverse('home_app:home'))

    else:
        form = UserLoginForm()
    return render(request, 'user_app/UserLogin.html', {'form': form})
def logoutUser(request):
    user = request.user
    logout(request, user)
    return redirect(reverse("user:login"))