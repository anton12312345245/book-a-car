from django.contrib import admin

from booking_cars.models import Car,Category,Booking

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Booking)