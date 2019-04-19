from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followings"
        )