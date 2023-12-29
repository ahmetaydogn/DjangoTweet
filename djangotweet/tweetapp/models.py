from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.username} {self.name} {self.surname}. Message: {self.message}"