from django.db import models
import geocoder

# Create your models here.


class Vessel(models.Model):
    name = models.CharField(max_length=100, null=True)
    callsign = models.CharField(max_length=20, null=True)
    destination = models.CharField(max_length=20, null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    datetime = models.DateTimeField(null=True)
    eta = models.TimeField(default=0)
    mmsi = models.FloatField(default=0)
    course = models.FloatField(default=0)
    speed = models.FloatField(default=0)
    heading = models.FloatField(default=0)
    navstat = models.FloatField(default=0)
    imo = models.FloatField(default=0)
    aistype = models.FloatField(default=0)
    a = models.PositiveIntegerField(default=0)
    b = models.PositiveIntegerField(default=0)
    c = models.PositiveIntegerField(default=0)
    d = models.PositiveIntegerField(default=0)
    draught = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Vessels'

    def save(self, *args, **kwargs):
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name