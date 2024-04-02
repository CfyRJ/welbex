from django.forms import ModelForm
from .models import Cars


class LocationsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ('car_number', 'location', 'lifting_capacity')
