from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


def log_in(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'GET':
        return render(request, 'login.html')

    email = request.POST.get('email').lower()
    user = authenticate(request, email=email, password=request.POST.get(key='password'))

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Wrong credentials')
        return render(request, 'login.html')


def log_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')
