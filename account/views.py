from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .models import User
# from django.core.checks import messages
from django.contrib.auth.decorators import login_required

from .models import Profile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/register')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=user_name, email=email, password=password)
            user.save()
            return redirect('/login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def user_profile(request):
    users = User.objects.all()
    profile = Profile.objects.get(user_id=request.user.id)
    context = {
        'profile': profile,
        'users': users,
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='/login')
def user_update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/update-profile.html', context)
