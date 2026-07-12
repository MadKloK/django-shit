from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get('next') or '/'
            return redirect(next_url)

        else:
            messages.error(request, "Invalid email, username or password.")

    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('/')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        
        else:
            messages.error(request, "Invalid Credentials.")

    else:
        form = CustomUserCreationForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)