from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length=2000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_01 = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"<id:{self.id} / nombre: {self.nombre} / apellido: {self.apellido} / edad: {self.edad} / profesion: {self.profesion} >"
