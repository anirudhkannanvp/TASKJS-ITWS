from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sensors(models.Model):
    sensor1 = models.FloatField(default=0)
    sensor2 = models.FloatField(default=0)
    def __str__(self):
        return str(self.sensor1) + ' ' + str(self.sensor2)