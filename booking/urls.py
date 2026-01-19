from django.urls import path
from .views import book, my_bookings
from .api import ListBooks

api_urls = [
    path('books',ListBooks.as_view(),name="list-books"),
]

urlpatterns = [
    path('book/', book, name='bookss'),
    path('my/', my_bookings, name='my_bookings'),
]


urlpatterns+=api_urls