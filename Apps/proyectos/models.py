from django.db import models

# Create your models here.

class Proyecto:
    nombre = models.CharField('Nombre del Proyecto',max_length = 50, unique=True)
    resumen = models.CharField('Resumen del Proyecto',max_length = 255, unique = True)
