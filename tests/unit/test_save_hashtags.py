import unittest
from unittest.mock import patch, Mock
from django.test import tag

from apps.twitter_clone.domain.hashtag import save_hashtags


@tag('unit')
class TestSaveHashtags(unittest.TestCase):
    @patch("apps.twitter_clone.models.Hashtag.objects.get_or_create")
    def test_save_hashtags(self, mock_get_or_create):
        mock_get_or_create.return_value = (Mock(), True)

        tweet = Mock(spec=['content'])
        tweet.content = 'Tweet #with #hashtags'

        save_hashtags(tweet)

        mock_get_or_create.assert_any_call(name='with')
        mock_get_or_create.assert_any_call(name='hashtags')

        mock_get_or_create.return_value[0].tweets.add.assert_called_with(tweet)

    @patch("apps.twitter_clone.models.Hashtag.objects.get_or_create")
    def test_save_hashtags_without_hashtag(self, mock_get_or_create):
        tweet = Mock(spec=['content'])
        tweet.content = 'Tweet without hashtag'

        save_hashtags(tweet)

        mock_get_or_create.assert_not_called()
