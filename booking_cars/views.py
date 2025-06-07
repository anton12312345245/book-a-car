from django.shortcuts import render
from booking_cars.models import Car,Category,Booking

def get_info(request):
    cars = Car.objects.all()
    context = {'Cars':cars}
    return render(request=request,template_name='Cars.html',context=context)
    