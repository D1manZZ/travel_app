from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.views.generic.edit import UpdateView
from .forms import *


def ez_life(request):
    return render(request, 'route/base.html')


class ShowCities(ListView):
    model = Cities
    paginate_by = 3
    context_object_name = 'cities'
    template_name = 'route/show_cities.html'


class ShowFlights(ListView):
    model = Planes
    paginate_by = 5
    context_object_name = 'flights'
    template_name = 'route/show_flights.html'


def show_city(request, pk):
    return render(request, 'route/city.html', {'city': get_object_or_404(Cities, id=pk)})


class ShowFlight(DetailView):
    model = Planes
    context_object_name = 'flight'
    template_name = 'route/flight.html'


class AddCity(CreateView):
    template_name = 'route/add_city.html'
    form_class = AddCity


class AddPlane(CreateView):
    template_name = 'route/add_plane.html'
    form_class = AddPlane


class UpdateCity(UpdateView):
    model = Cities
    form_class = EditCity
    template_name = 'route/cities_update_form.html'


class UpdateFlight(UpdateView):
    template_name = 'route/flight_update.html'
    model = Planes
    form_class = EditPlane


class DeleteCity(DeleteView):
    model = Cities
    success_url = reverse_lazy('cities')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class DeleteFlight(DeleteCity):
    model = Planes
    success_url = reverse_lazy('flights')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
