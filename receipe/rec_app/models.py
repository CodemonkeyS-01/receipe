from django.db import models


# Create your models here.
class Receipes(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.name}"

class Container(models.Model):
    ingredients = models.CharField(max_length=500)
    procedure = models.CharField(max_length = 1000)
    receipe = models.ForeignKey(Receipes, on_delete = models.CASCADE, null = True, blank=True, related_name="container")

    def __str__(self):
        return f"Container:{self.id}"

