from django.db import models

# Create your models here.
class Pet(models.Model):
    animal_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    adopted = models.BooleanField(default=False)
