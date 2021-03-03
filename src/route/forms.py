from django import forms
from .models import Cities


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

