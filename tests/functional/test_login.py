from django.test import TestCase, Client

from apps.authentication.models import User


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            email='test@test.fr',
            password='1234',
            username='username-test',
            first_name='test'
        )

    def test_login_wrong_credentials(self):
        response = self.client.post('/login/', {'email': 'test@test.fr', 'password': 'abcd'})

        self.assertIn("Wrong credentials", response.content.decode())

    def test_login(self):
        response = self.client.post('/login/', {'email': 'test@test.fr', 'password': '1234'})

        self.assertRedirects(response, '/')
