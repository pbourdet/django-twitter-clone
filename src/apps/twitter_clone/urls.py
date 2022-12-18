from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_tweet", views.create_tweet, name="create_tweet"),
    path("hashtag/<str:hashtag_name>", views.hashtag_tweets, name="hashtag_tweets"),
]
