from django.forms import ModelForm
from .models import Locations


class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = ('zip', 'lat', 'lng', 'city', 'state_name')
