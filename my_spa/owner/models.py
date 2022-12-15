from django.db import models
from customer.models import *
class Memberships(models.Model):
    name = models.CharField(max_length=150,unique=True)
    validity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True)
    status=models.BooleanField(default=True,null=True)


    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=150,unique=True)
    price = models.PositiveIntegerField(null=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True)
    status=models.BooleanField(default=True,null=True)
    timeslot=models.ForeignKey(Timeslots,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

