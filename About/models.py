from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length = 100)

    def __str__(self):
        return f"<id:{self.id} / nombre: {self.nombre} / apellido: {self.apellido} / edad: {self.edad} / profesion: {self.profesion} >"
