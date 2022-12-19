import unittest
from django.test import tag

from apps.twitter_clone.templatetags.filters import display_tweet


@tag("unit")
class TestFilters(unittest.TestCase):
    def test_display_tweet(self):
        tweet_content = display_tweet("This is the content #CONTENT")
        self.assertEqual(
            tweet_content,
            "This is the content "
            '<a style="text-decoration: none" href="/hashtag/content">#CONTENT</a>',
        )

        tweet_content = display_tweet("This is the content #/CONTENT")
        self.assertEqual(tweet_content, "This is the content #/CONTENT")
