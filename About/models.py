from django.db import models

# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length = 100)

    def __str__(self):
        return f"Nombre {self.nombre}, Apellido {self.apellido}, Edad {self.edad}, profesión {self.profesion}"
