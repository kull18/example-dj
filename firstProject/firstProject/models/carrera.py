from django.db import models

class Carrera(models.Model):
    nombre=models.CharField(max_length=20); 
    descripcion=models.TextField(max_length=20, blank=True, null=True);
    def __str__(self):
        return self.nombre;  