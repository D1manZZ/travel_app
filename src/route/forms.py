from django import forms
from .models import Cities, Planes


class AddCity(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['city', 'description', 'photo']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class EditCity(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['city', 'description', 'photo']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddPlane(forms.ModelForm):
    class Meta:
        model = Planes
        fields = ['plain_code', 'plain_start', 'plain_end', 'trip_time']
        widgets = {
            'plain_code': forms.TextInput(attrs={'class': 'form-control'}),
            'plain_start': forms.Select(attrs={'class': 'form-control'}),
            'plain_end': forms.Select(attrs={'class': 'form-control'})
        }


class EditPlane(forms.ModelForm):
    class Meta:
        model = Planes
        fields = ['plain_code', 'plain_start', 'plain_end', 'trip_time']
        widgets = {
            'plain_code': forms.TextInput(attrs={'class': 'form-control'}),
            'plain_start': forms.Select(attrs={'class': 'form-control'}),
            'plain_end': forms.Select(attrs={'class': 'form-control'})
        }