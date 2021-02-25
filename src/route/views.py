from django.shortcuts import render, get_object_or_404
from .models import *


def ez_life(request):
    return render(request, 'route/base.html')


def show_cities(request):
    cities = Cities.objects.all()
    return render(request, 'route/show_cities.html', {'cities': cities})


def show_city(request, pk):
    return render(request, 'route/city.html', {'city': get_object_or_404(Cities, id=pk)})

