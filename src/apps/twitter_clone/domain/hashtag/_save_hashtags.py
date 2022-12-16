import re

from apps.twitter_clone.models import Hashtag, Tweet


def save_hashtags(tweet: Tweet) -> None:
    for hashtag_name in re.findall(r'#\w+', tweet.content):
        hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_name.lower()[1:])
        hashtag.tweets.add(tweet)
