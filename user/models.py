from django.db import models
from django.contrib.auth.models import BaseUserManager

class Users(models.Model):
    username = models.CharField(max_length = 20, unique=True)
    email = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length=25)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.username