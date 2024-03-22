from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # New field to store creation timestamp
    # Add any additional fields you need

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Response(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Session(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    num_engagements = models.IntegerField(default=0)
    num_trials = models.IntegerField(default=0)

    def __str__(self):
        return f"Session for {self.client.first_name} {self.client.last_name}"