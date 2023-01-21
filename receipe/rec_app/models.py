from django.db import models


# Create your models here.
class Receipes(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    ingredients = models.CharField(max_length=500)
    procedure = models.CharField(max_length = 1000)