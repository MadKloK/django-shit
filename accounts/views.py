from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get('next') or '/'
            return redirect(next_url)

        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    # if request.user.is_authenticated:
    logout(request)
    return redirect('/')

def register_view(request):
    return render(request, 'accounts/register.html')