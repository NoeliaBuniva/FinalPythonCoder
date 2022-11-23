from django.db import models

class recetas(models.Model):
    comida = models.CharField(max_length = 200)
    ingredientes = models.CharField(max_length = 200)
    preparación = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    receta_imagen = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Receta de: {self.comida}"

class FichaSocio(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 20)
    edad = models.IntegerField()
    descripcion = models.TextField(max_length=2000)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    imagen01 = models.ImageField(upload_to="photos", null=True, blank=True)

    def __str__(self):
        return f"<{self.imagen01}/ nombre: {self.nombre} / apellido: {self.apellido} / edad: {self.edad} >"


class entrenamientos(models.Model):
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
    sexo_opciones = [
        (femenino, "Femenino"),
        (masculino, "Masculino"),
    ]
    sexo = models.CharField(max_length = 2, choices = sexo_opciones) 

    def __str__(self):
        return f"<Grupo muscular: {self.grupo_muscular} / Sexo: {self.sexo}>"
    

class rutina(models.Model):
    ejercicios = models.CharField(max_length = 80, default = "no hay rutina todavía")

    def __str__(self):
        return f"<Ejercicios: {self.ejercicios}>"


class horarios(models.Model): 
    lunes = "Lunes"
    martes = "Martes"
    miércoles = "Miércoles"
    jueves = "Jueves"
    viernes = "Viernes"
    día_opciones = [
        (lunes, "Lunes"),
        (martes, "Martes"),
        (miércoles, "Miércoles"),
        (jueves, "Jueves"),
        (viernes, "Viernes"),
    ]
    día = models.CharField(max_length = 10, choices = día_opciones) 

    belgrano = "Belgrano"
    nuñez = "Nuñez"
    palermo = "Palermo"
    sede_opciones = [
        (belgrano, "Belgrano"),
        (nuñez, "Nuñez"),
        (palermo, "Palermo"),
    ]
    sede = models.CharField(max_length = 20, choices = sede_opciones) 

    yoga = "Yoga"
    meditación = "Meditación"
    clase_opciones = [
        (yoga, "Yoga"),
        (meditación, "Meditación")
    ]
    clase = models.CharField(max_length = 20, choices = clase_opciones)
    
    
    ocho = "8hs"
    nueve = "9hs"
    diez = "10hs"
    once = "11hs"
    doce = "12hs"
    horario_opciones = [
        (ocho, "8 hs"),
        (nueve, "9 hs"),
        (diez, "10 hs"),
        (once, "11 hs"),
        (doce, "12 hs"),
    ]
    horario = models.CharField(max_length = 5, choices = horario_opciones)

    def __str__(self):
        return f"Día: {self.día} / Sede: {self.sede} / Clase: {self.clase} / Horario: {self.horario}"