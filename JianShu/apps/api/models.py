from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(max_length=1000, blank=False)
    auth = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

