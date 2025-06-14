from django.urls import path,include
from booking_cars import views

urlpatterns = [
    path('',views.main_filter,name='cars')
]
 
