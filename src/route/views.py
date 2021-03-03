from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import *
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from .forms import AddCity, EditCity


def ez_life(request):
    return render(request, 'route/base.html')


# def show_cities(request):
#     cities = Cities.objects.all()
#     return render(request, 'route/show_cities.html', {'cities': cities})


class ShowCities(ListView):
    model = Cities
    paginate_by = 3
    context_object_name = 'cities'
    template_name = 'route/show_cities.html'


def show_city(request, pk):
    return render(request, 'route/city.html', {'city': get_object_or_404(Cities, id=pk)})


class AddCity(CreateView):
    template_name = 'route/add_city.html'
    form_class = AddCity


class UpdateCity(UpdateView):
    model = Cities
    form_class = EditCity
    template_name = 'route/cities_update_form.html'


class DeleteCity(DeleteView):
    model = Cities
    success_url = reverse_lazy('cities')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
