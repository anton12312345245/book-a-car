from django.urls import path,include
from booking_cars import views


urlpatterns = [
    path('',views.get_info,name='cars')
]
 
