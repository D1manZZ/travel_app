from .views import *
from django.urls import path

urlpatterns = [
    path('', ez_life, name='main_page'),
    path('cities/', ShowCities.as_view(), name='cities'),
    path('city/<int:pk>/', show_city, name='city'),
    path('add_city/', AddCity.as_view(), name='add_city'),
    path('edit_city/<int:pk>/', UpdateCity.as_view(), name='update_city'),
    path('delete_city/<int:pk>/', DeleteCity.as_view(), name='delete_city'),
    path('flights/', ShowFlights.as_view(), name='flights'),
    path('add_plane/', AddPlane.as_view(), name='add_plane'),
    path('flight/<int:pk>/', ShowFlight.as_view(), name='flight'),
    path('edit_flight/<int:pk>/', UpdateFlight.as_view(), name='edit_flight'),
    path('delete_flight/<int:pk>/', DeleteFlight.as_view(), name='delete_flight')
]
