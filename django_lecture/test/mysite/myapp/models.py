from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Test(models.Model):
    choices = [('U','User'),('S','Seller'),('B','Broker')]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=1,choices=choices,default='none')
    phone_number = models.CharField(max_length=5)
    is_user= models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    
    def get_absolute_url(self):
        return reverse('estate_detail',kwargs={'pk':self.pk})

class Estate(models.Model):
    broker = models.ForeignKey(Test,on_delete=models.CASCADE)
    price = models.FloatField()
    bedroom = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    area = models.IntegerField()
    def __str__(self):
        return self.broker.user.username

    def get_absolute_url(self):
        return reverse('estate_detail',kwargs={'pk':self.pk})
