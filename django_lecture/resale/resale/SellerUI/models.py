from django.db import models

# Create your models here.

class Vehicle(models.Model):
    fueltanktypes = [
        ('P','Petrol'),
        ('D','Diesel'),
        ('C','CNG')
    ]
    Vmodel = models.CharField(max_length = 50)
    make = models.CharField(max_length = 20)
    desc = models.TextField()
    age = models.IntegerField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    fueltank = models.CharField(max_length = 1, choices = fueltanktypes, default = 'P')
    price = models.IntegerField(blank = True,default= 0)

    def __str__(self):
        return f'{self.Vmodel} {self.make}'





