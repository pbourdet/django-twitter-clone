from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

from .domain import hashtag as hashtag_module
from .forms import TweetForm
from .models import Tweet, Hashtag


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
        tweet = Tweet.objects.create(
            content=tweet_form.cleaned_data['content'],
            user=request.user
        )

        hashtag_module.save_hashtags(tweet)

    return redirect('home')


@require_http_methods(['GET'])
def hashtag_tweets(request: HttpRequest, hashtag_name: str) -> HttpResponse:
    try:
        hashtag = Hashtag.objects.get(name=hashtag_name)
    except Hashtag.DoesNotExist:
        hashtag = None

    return render(request, 'pages/hashtag.html', {'hashtag': hashtag})
