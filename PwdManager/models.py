from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Account object
class Account(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title
