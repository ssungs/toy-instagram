from django.db import models
from django.contrib.auth.models import User
from behavior import BaseField


class UserProfile(BaseField):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)
    name = models.CharField(max_length=64)
    introduce_text = models.TextField()
