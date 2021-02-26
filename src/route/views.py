from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import CreateView
from .forms import AddCity


def ez_life(request):
    return render(request, 'route/base.html')


def show_cities(request):
    cities = Cities.objects.all()
    return render(request, 'route/show_cities.html', {'cities': cities})


def show_city(request, pk):
    return render(request, 'route/city.html', {'city': get_object_or_404(Cities, id=pk)})


class AddCity(CreateView):
    template_name = 'route/add_city.html'
    form_class = AddCity
