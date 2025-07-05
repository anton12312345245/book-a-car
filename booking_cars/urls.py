from django.urls import path,include
from booking_cars import views

urlpatterns = [
    path('',views.main_filter,name='cars'),
    path('/car/<int:id>/',views.car_details,name='Car details'),
    path('/car/<int:id>/book',views.book_car,name='Book car')
]

 
