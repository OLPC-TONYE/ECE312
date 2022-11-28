import math
from django.db import models

class Calculation(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date_calculated')
   
    def __str__(self):
        return self.title

class Variables(models.Model):
    calculation = models.OneToOneField(Calculation, on_delete=models.CASCADE, primary_key=True)
    electrical_mobility = models.FloatField('dm')
    mass = models.FloatField('m')

    def get_result(self):
        return (6 * self.mass)/(math.pi * (self.electrical_mobility)**3)

    def __str__(self):
        return "Electrical Mobility: %f,  Mass= %f" % (self.electrical_mobility, self.mass)