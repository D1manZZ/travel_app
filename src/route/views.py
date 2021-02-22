from django.shortcuts import render
from .models import *


def ez_life(request):
    return render(request, 'route/base.html')


def show_cities(request):
    cities = Cities.objects.all()
    return render(request, 'route/show_cities.html', {'cities': cities})
