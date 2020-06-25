from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Broker(models.Model):
    firstname = models.CharField(max_length = 25)
    lastname = models.CharField(max_length = 25)
    username = models.CharField(max_length = 25, unique=True)
    email = models.EmailField(max_length = 25)
    password = models.CharField(max_length = 25, )
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

