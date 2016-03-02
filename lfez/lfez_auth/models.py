#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


class lfezUser(AbstractUser):
    intro = models.CharField(max_length=200, blank=True, )


