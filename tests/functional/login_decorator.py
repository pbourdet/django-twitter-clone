from functools import wraps

from apps.authentication.models import User


def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        User.objects.create_user('testuser', 'test@test.fr', '1234')
        self.client.login(email='test@test.fr', password='1234')

        return func(self, *args, **kwargs)

    return wrapper
