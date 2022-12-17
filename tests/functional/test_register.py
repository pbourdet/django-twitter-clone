from django.test import TestCase, tag

from apps.authentication.models import User
from .login_decorator import login_required


@tag('functional')
class RegisterTestCase(TestCase):
    def setUp(self) -> None:
        self.valid_payload = {
            'email': 'test@aze.fr',
            'first_name': 'aze',
            'username': 'aze',
            'password': 'aze',
            'password_confirmation': 'aze'
        }

    @login_required
    def test_register_logged_in(self) -> None:
        response = self.client.get('/register/')

        self.assertRedirects(response, '/')

    def test_register_get_form(self) -> None:
        response = self.client.get('/register/')

        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password confirmation')

    def test_register_missing_data(self) -> None:
        for key in self.valid_payload:
            payload = dict(self.valid_payload)
            payload.pop(key)
            response = self.client.post('/register/', payload)

            self.assertEqual(0, User.objects.all().count())
            self.assertFormError(response, 'form', key, 'This field is required.')

    def test_register_invalid_email(self) -> None:
        self.valid_payload['email'] = 'invalid email'

        response = self.client.post('/register/', self.valid_payload)

        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertEqual(0, User.objects.all().count())

    def test_register_invalid_username(self) -> None:
        self.valid_payload['username'] = 'invalid /^username/'

        response = self.client.post('/register/', self.valid_payload)

        self.assertFormError(
            response,
            'form',
            'username',
            'Username may only contain letters, digits, and the following characters: . + - _'
        )
        self.assertEqual(0, User.objects.all().count())

    def test_register_invalid_password(self) -> None:
        self.valid_payload['password_confirmation'] = '1234'

        response = self.client.post('/register/', self.valid_payload)

        self.assertFormError(response, 'form', 'password_confirmation', 'Passwords do not match')
        self.assertEqual(0, User.objects.all().count())

    def test_register(self) -> None:
        response = self.client.post('/register/', self.valid_payload)

        self.assertRedirects(response, '/')
        self.assertEqual(1, User.objects.all().count())
