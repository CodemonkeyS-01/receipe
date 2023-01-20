from django.db import models

# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=500)
    procedure = models.CharField(max_length = 1000)