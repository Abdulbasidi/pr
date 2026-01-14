from django.urls import path
from .import views
from .views import main_page,contacts,about,works,services,offers

urlpatterns = [
    path('',main_page, name = "main-page"),
    path('contact',contacts),
    path('about',about),
    path('services',services),
    path('works',works),
    path('offers',offers),
]