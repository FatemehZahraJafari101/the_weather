from django import forms
from django.forms import ModelForm
from .models import WeatherModel

class WeatherForm(ModelForm):
    class Meta():
        model = WeatherModel
        fields = '__all__'

        labels = {
            "city" : '',
        }

        widgets = {
            'city' : forms.TextInput(attrs={'class' : 'flex-form' , 'placeholder' : 'City Name   '})
        }