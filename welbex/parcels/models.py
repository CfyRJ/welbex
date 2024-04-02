from django.db import models
from ..location.models import Locations


class Parcels(models.Model):
    location_pick_up = models.ForeignKey(Locations,
                                         on_delete=models.PROTECT,
                                         related_name='locations_pick_up',
                                         verbose_name=('Pick-up'))
    location_delivery = models.ForeignKey(Locations,
                                          on_delete=models.PROTECT,
                                          related_name='locations_delivery',
                                          verbose_name=('Delivery'))
    weight = models.IntegerField()
    description = models.TextField(verbose_name=('Description'))

    def __str__(self) -> str:
        return self.description
