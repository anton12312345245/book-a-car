from django.shortcuts import render
from booking_cars.models import Car,Category,Booking
from datetime import datetime
from django.db.models import Q


def get_info(request):
    cars = Car.objects.all()
    context = {'Cars':cars}
    return render(request=request,template_name='Cars.html',context=context)


def main_filter(request):
    category = Category.objects.all()
    selected_category = request.GET.get('category',None)
    min_price = request.GET.get('min price',None)
    max_price = request.GET.get('max price',None)
    year = request.GET.get('year',None)
    air_conditioning = request.GET.get('air condition',None)
    location = request.GET.get('location',None)
    start_time = request.GET.get('start time',None)
    end_time = request.GET.get('end time',None)
    


    cars = Car.objects.all()
    if selected_category:
        cars = cars.filter(type__id=selected_category)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if year:
        cars = cars.filter(year__gte=year)
    if air_conditioning == 'Yes':
        cars = cars.filter(air_condition=True)
    elif air_conditioning == 'No':
        cars = cars.filter(air_condition=False)
    # if location:
    #     cars = cars.filter(location=location)
    if start_time and end_time:
        try:
            start_date = datetime.strptime(start_time, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_time, '%Y-%m-%d').date()
            # Виключаємо автомобілі, які мають бронювання, що перетинаються з обраними датами
            booked_cars = Booking.objects.filter(
                Q(start_time__lte=end_date) & Q(end_time__gte=start_date)
            ).values_list('which_car__id', flat=True)
            cars = cars.exclude(id__in=booked_cars)
        except ValueError:
            pass
    
    context = {
    'cars':cars,
    'categories':category,
    'selected_category':selected_category,
    'min_price':min_price,
    'max_price':max_price,
    'year':year,
    'air_condition':air_conditioning,
    'location':location,
    'start_time':start_time,
    'end_time':end_time
    } 
    

    return render(request=request,template_name='Filtred_cars.html',context=context)