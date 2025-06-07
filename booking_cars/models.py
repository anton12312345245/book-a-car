from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    rating = models.FloatField()
    transmission = models.CharField(max_length=100)
    air_conditioning = models.BooleanField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
    type = models.ForeignKey(Category,on_delete=models.CASCADE)


class Booking(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Bookings')
    location = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    which_car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.User.username}-{self.which_car}'