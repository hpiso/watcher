from __future__ import unicode_literals

from django.db import models

class Object(models.Model):
    mac_address = models.CharField(max_length=200)
    date_time = models.DateTimeField()

