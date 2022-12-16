from django.test import TestCase, Client, tag
from django.urls import reverse

from apps.twitter_clone.models import Tweet, Hashtag
from .login_decorator import login_required


@tag('functional')
class CreateTweetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_tweet')

    def test_creation_without_login(self):
        response = self.client.post(self.url, {'content': 'hello'})

        self.assertRedirects(response, '/login/?next=%2Fcreate_tweet')

    @login_required
    def test_creation_with_content_too_long(self):
        response = self.client.post('/create_tweet', {'content': '0' * 300})

        self.assertRedirects(response, '/')

        self.assertEqual(0, Tweet.objects.all().count())

    @login_required
    def test_creation(self):
        response = self.client.post('/create_tweet', {'content': 'Tweet #created'})

        self.assertRedirects(response, '/')
        self.assertEqual(1, Tweet.objects.all().count())
        self.assertEqual(1, Hashtag.objects.all().count())
