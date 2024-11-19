from django.db import models

# Create your models here.

class Gamerinfo(models.Model):
    username = models.CharField(max_length=58)
    state = models.CharField(max_length=28)
    region = models.CharField(max_length=18)