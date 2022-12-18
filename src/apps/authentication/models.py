from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    class Meta:
        db_table = "auth_user"
