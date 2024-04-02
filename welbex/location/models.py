from django.db import models


class Locations(models.Model):
    zip = models.IntegerField(unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    city = models.CharField(max_length=50, verbose_name="City")
    state_name = models.CharField(max_length=50, verbose_name="State")

    def __str__(self) -> str:
        return self.city
