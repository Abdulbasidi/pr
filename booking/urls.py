from django.urls import path
from .views import book, my_bookings
from .api import ListBooks

api_urls = [
    path('booksapi',ListBooks.as_view(),name="list-books"),
]

urlpatterns = [
    path('book/', book, name='book'),
    path('my/', my_bookings, name='my_bookings'),
]


urlpatterns+=api_urls