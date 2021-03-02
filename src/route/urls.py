from .views import *
from django.urls import path

urlpatterns = [
    path('', ez_life, name='main_page'),
    path('cities/', ShowCities.as_view(), name='cities'),
    path('city/<int:pk>/', show_city, name='city'),
    path('add_city/', AddCity.as_view(), name='add_city'),
    path('edit_city/<int:pk>/', UpdateCity.as_view(), name='update_city'),
    path('delete_city/<int:pk>/', DeleteCity.as_view(), name='delete_city')
]
