# models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)

class Response(models.Model):
    name = models.CharField(max_length=255)
    num_engagements = models.IntegerField(default=0)

class Session(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    engagements = models.IntegerField(default=0)
    num_trials = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
