from django.db import models
from django.utils import timezone

class Activity(models.Model):
    name = models.CharField(max_length=100, default='Valor predeterminado')
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)  # Asignando la fecha y hora actual como valor predeterminado

    def __str__(self):
        return self.name