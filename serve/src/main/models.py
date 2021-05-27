from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import json

# Create your models here.
class dashitem(models.Model):
    name = models.CharField(max_length=64, default='')
    memo = models.TextField(max_length=64, default='')
    enable = models.BooleanField(default=False)
    asdefault = models.BooleanField(default=False)
    owner = models.TextField(default='*', null=True)
    menuindex = models.IntegerField(default=100)

    class Meta:
        ordering = ('name',)

    def getJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,  sort_keys=True, indent=4)

    def __str__(self):  # python 3
        return self.name

class loginfo(models.Model):
    user = models.CharField(max_length=64, default='')
    logdate = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=64, default='', null=True)
    status = models.CharField(max_length=64, default='', null=True)
    addr = models.CharField(max_length=64, default='', null=True)
    os = models.CharField(max_length=64, default='', null=True)
    osver = models.CharField(max_length=64, default='', null=True)
    browser = models.CharField(max_length=64, default='', null=True)
    browserver = models.CharField(max_length=64, default='', null=True)
    device = models.CharField(max_length=64, default='', null=True)
    memo = models.TextField(default='', null=True)

    class Meta:
        ordering = ('logdate', 'user')

    def getJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):  # python 3
        return self.user


class apiinfo(models.Model):
    user = models.CharField(max_length=64, default='')
    indate = models.DateTimeField(default=timezone.now)
    outdate = models.DateTimeField(default=timezone.now)
    addr = models.CharField(max_length=64, default='', null=True)
    status = models.CharField(max_length=64, default='', null=True)
    tool = models.CharField(max_length=64, default='', null=True)
    model = models.CharField(max_length=64, default='', null=True)
    api = models.CharField(max_length=64, default='', null=True)
    param = models.TextField(default='', null=True)
    desc = models.TextField(default='', null=True)

    class Meta:
        ordering = ('indate', 'user')

    def getJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __str__(self):  # python 3
        return self.user