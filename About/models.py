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


class entrenamientos(models.Model):
    ejercicios = models.CharField(max_length = 80, default = "no hay rutina todavía")
    tren_superior  = "TS"
    tren_inferior = "TI"
    core = "C"
    grupo_muscular_opciones = [
        (tren_superior, "Tren Superior"),
        (tren_inferior, "Tren Inferior"),
        (core, "Core"),
    ]
    grupo_muscular = models.CharField(max_length = 2, choices = grupo_muscular_opciones) 
    
    
    femenino = "F"
    masculino = "M"
    otro = "O"
    sexo_opciones = [
        (femenino, "Femenino"),
        (masculino, "Masculino"),
        (otro, "Otro"),
    ]
    sexo = models.CharField(max_length = 2, choices = sexo_opciones) 

    def __str__(self):
        return f"<Grupo muscular: {self.grupo_muscular} / Sexo: {self.sexo} / Ejercicios: {self.ejercicios}>"
    

class rutina(models.Model):
    ejercicios = models.CharField(max_length = 80, default = "no hay rutina todavía")

    def __str__(self):
        return f"<Ejercicios: {self.ejercicios}>"