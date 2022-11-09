from django.db import models

class FichaSocio(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 20)
    edad = models.IntegerField()
    descripcion = models.TextField(max_length=2000)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    imagen01 = models.ImageField(upload_to="photos", null=True, blank=True)

    def __str__(self):
        return f"<id:{self.id} / nombre: {self.nombre} / apellido: {self.apellido} / edad: {self.edad} >"

