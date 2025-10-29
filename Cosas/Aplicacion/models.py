from django.db import models
from django.db import date


# Create your models here.
class producto (models.models):
    nombre =models.CharField(max_lenght=40)
    precio =models.CharField(max_lenght=15)
    descripcion =models.CharField(max_lenght=130)
    fecha =models.DateField()
    cantidad =models.CharField(max_lenght=5)

def __str__(self):
   return self.nombre
