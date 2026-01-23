from django.urls import path
from .views import book, my_bookings
from .api import ListBooking, DetailBooking

api_urls = [
    path('booksapi',ListBooking.as_view(),name="list-books"),
    path('bookings/<int:id>/', DetailBooking.as_view()),
]

urlpatterns = [
    path('bookpost/', book, name='bookpost'),
    path('my/', my_bookings, name='my_bookings'),
]


urlpatterns+=api_urls