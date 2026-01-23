from django.urls import path,include
from .views import book, my_bookings
from .api import ListBooking, DetailBooking,BookingViewSet
from rest_framework.routers import DefaultRouter
routers = DefaultRouter()

routers.register('api/books',BookingViewSet,basename="apibooks")



api_urls = [
    path('booksapi',ListBooking.as_view(),name="list-books"),
    path('bookings/<int:id>/', DetailBooking.as_view()),
    path('',include(routers.urls))
]




urlpatterns = [
    path('bookpost/', book, name='bookpost'),
    path('my/', my_bookings, name='my_bookings'),
]


urlpatterns+=api_urls