from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Tweet


def home(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all()
    context = {'tweets': tweets}
    return render(request, 'pages/home.html', context=context)
