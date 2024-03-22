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