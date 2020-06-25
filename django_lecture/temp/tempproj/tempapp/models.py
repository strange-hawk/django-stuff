from django.db import models

# Create your models here.
class BirthPlace(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=200)
    birthplace = models.ForeignKey(BirthPlace,on_delete=models.CASCADE)
