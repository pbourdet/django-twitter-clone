from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from apps.authentication.forms import RegistrationForm, LoginForm
from apps.authentication.models import User


@require_http_methods(["GET", "POST"])
def log_in(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "form/login.html", {"form": LoginForm()})

    email = request.POST.get("email").lower()
    user = authenticate(request, email=email, password=request.POST.get(key="password"))

    if user is None:
        messages.error(request, "Wrong credentials")
        return render(request, "form/login.html", {"form": LoginForm()})

    login(request, user)
    return redirect("home")


@require_http_methods(["GET"])
def log_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("home")


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "GET":
        return render(request, "form/register.html", {"form": RegistrationForm()})

    registration_form = RegistrationForm(request.POST or None)

    if not registration_form.is_valid():
        return render(request, "form/register.html", {"form": registration_form})

    cleaned_data = registration_form.cleaned_data

    user = User(
        email=cleaned_data["email"],
        username=cleaned_data["username"],
        first_name=cleaned_data["first_name"],
        last_name=cleaned_data["last_name"],
    )
    user.set_password(cleaned_data["password"])
    user.save()

    login(request, user)
    return redirect("home")
