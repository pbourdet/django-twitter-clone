from django.db import models

from apps.authentication.models import User


class Tweet(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(default=None, null=True, blank=True)
