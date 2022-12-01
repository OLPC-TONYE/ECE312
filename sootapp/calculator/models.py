import math

from django.db import models
from django.utils import timezone

class Calculation(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date_calculated')
   
    def __str__(self):
        return self.title

class Variables(models.Model):
    calculation = models.ForeignKey(Calculation, on_delete=models.CASCADE)
    electrical_mobility = models.FloatField('dm', default=0)
    mass = models.FloatField('m', default=1)
    def get_result(self):
        result = (6 * self.mass)/(math.pi * (self.electrical_mobility)**3)
        return result

    def __str__(self):
        return "Electrical Mobility: %f,  Mass= %f" % (self.electrical_mobility, self.mass)