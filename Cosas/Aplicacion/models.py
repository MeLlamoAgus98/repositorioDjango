from django.db import models
from datetime import date


class Producto(models.Model):  
    nombre = models.CharField(max_length=40)       
    precio = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=130)
    fecha = models.DateField(default=date.today)   
    cantidad = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre
