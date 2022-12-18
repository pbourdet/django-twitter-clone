from django.test import TestCase, Client, tag

from apps.authentication.models import User
from apps.twitter_clone.models import Tweet, Hashtag


@tag('functional')
class CreateTweetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('testuser', 'test@test.fr', '1234')
        hashtag = Hashtag.objects.create(name='test')
        tweet = Tweet.objects.create(content='testing #test', user=user)
        hashtag.tweets.add(tweet)

    def test_hashtag_without_tweets(self):
        response = self.client.get('/hashtag/nothing')

        self.assertContains(response, 'Nothing matches your search')

    def test_hashtag_wit_tweets(self):
        response = self.client.get('/hashtag/test')

        self.assertContains(response, 'testing #test')
