from .views import *
from django.urls import path

urlpatterns = [
    path('', ez_life, name='main_page')
]
