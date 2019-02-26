from django.db import models
from django.contrib.auth.models import User


class Bloguser(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    #昵称
    nickname = models.CharField(max_length=50, blank=True)

