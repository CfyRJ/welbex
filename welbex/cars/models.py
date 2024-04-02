from django.db import models
from ..location.models import Locations


class Cars(models.Model):
    car_number = models.CharField(max_length=5, unique=True, verbose_name=('Car number'))
    location = models.ForeignKey(Locations,
                                 on_delete=models.PROTECT,
                                 related_name='locations_cars',
                                 verbose_name=('Location'))
    lifting_capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.car_number
