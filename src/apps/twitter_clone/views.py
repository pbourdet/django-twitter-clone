from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from .forms import TweetForm
from .models import Tweet


@require_http_methods(['GET'])
def home(request: HttpRequest) -> HttpResponse:
    tweets = Tweet.objects.all().order_by('-created_at')
    form = TweetForm()

    context = {'tweets': tweets, 'form': form}

    return render(request, 'pages/home.html', context=context)


@login_required
@require_http_methods(['POST'])
def create_tweet(request: HttpRequest) -> HttpResponse:
    tweet_form = TweetForm(request.POST or None)

    if tweet_form.is_valid():
        Tweet.objects.create(
            content=tweet_form.cleaned_data['content'],
            user=request.user
        )

    return redirect('home')
