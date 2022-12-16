from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime

# Create your models here.
available_service = []
booked_service=[]
class Categories(models.Model):
    category_name = models.CharField(max_length=140, unique=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.category_name

class Beautician(models.Model):
    name=models.CharField(max_length=150)
    options=(
        ("male","male"),
        ("female","female"),

    )
    gender=models.CharField(max_length=150,choices=options)
    tenure=models.PositiveIntegerField(default=1)
    category=models.ManyToManyField(Categories,blank=True)
    options=(
        ("available","available"),
        ("unavailable","unavailable")
    )
    status=models.CharField(max_length=150,choices=options,default="available")

    def __str__(self):
        return self.name

class Timeslots(models.Model):
    time=models.CharField(max_length=200,unique=True)
    options=(
        ("available","available"),
        ("pending","pending"),
        ("booked","booked"),)

    status=models.CharField(max_length=100,choices=options,default="available")

    def __str__(self):
        return self.time


class Services(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/",null=True)
    duration=models.DurationField(null=True, blank=True)
    cost=models.PositiveIntegerField()
    description=models.CharField(max_length=250,null=True,blank=True)
    beautician=models.ManyToManyField(Beautician)
    status=models.BooleanField(default=True)
    rating=models.PositiveIntegerField(default=5)
    timeslots=models.ManyToManyField(Timeslots)


    SERVICE_TIMESLOT_LIST = [
        ('09:00 AM – 09:30 AM','09:00 AM – 09:30 AM'),
        ('10:00 AM – 10:30 AM', '10:00 AM – 10:30 AM'),
        ('11:00 AM – 11:30 AM', '11:00 AM – 11:30 AM'),
        ('12:00 PM – 12:30 PM', '12:00 PM – 12:30 PM'),
        ('13:00 PM – 13:30 PM', '13:00 PM – 13:30 PM'),
        ('14:00 PM – 14:30 PM', '14:00 PM – 14:30 PM'),
        ('15:00 PM – 15:30 PM', '15:00 PM – 15:30 PM'),
        ('16:00 PM – 16:30 PM', '16:00 PM – 16:30 PM'),
        ('17:00 PM – 17:30 PM', '17:00 PM – 17:30 PM'),
    ]
    availability=models.IntegerField(choices=SERVICE_TIMESLOT_LIST,blank=True,null=True)

    def __str__(self):
        return self.name

class BookedSlot(models.Model):
    booked_slots = models.CharField(max_length=260,unique=True)
    def __str__(self):
        return self.booked_slots


class Booking(models.Model):

    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(null=True,auto_now_add=True)
    timeslot = models.ForeignKey(BookedSlot,on_delete=models.CASCADE,null=True)
    beautician=models.ForeignKey(Beautician,on_delete=models.CASCADE)
    cost=models.PositiveIntegerField()
    options = (
                ("booked","booked"),
                ("booking-confirmed", "booking-confirmed"),
                ("cancelled","cancelled"),
                ("completed", "completed"),

            )
    status=models.CharField(max_length=200, choices=options, default="booked")


class GiftCards(models.Model):
    name = models.CharField(max_length=300)
    validity = models.PositiveIntegerField()
    desc = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    img = models.ImageField(upload_to="images/",null=True)
    options = (
        ("available", "available"),
        ("booked", "booked"),
        ("not available", "not available")
    )
    status = models.CharField(max_length=200, choices=options, default="available")


    





