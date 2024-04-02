from django.forms import ModelForm
from .models import Parcels


class ParcelsForm(ModelForm):
    class Meta:
        model = Parcels
        fields = ('location_pick_up', 'location_delivery',
                  'weight', 'description')
