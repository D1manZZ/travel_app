from .views import *
from django.urls import path

urlpatterns = [
    path('', ez_life, name='main_page'),
    path('cities/', show_cities, name='cities'),
    path('city/<int:pk>/', show_city, name='city')
]
