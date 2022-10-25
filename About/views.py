from django.shortcuts import render
from django.views import View
from About.models import Administrador


# Create your views here.

class ListaPostulantes(View):
    template_name = "About/lista_postu.html"

    def get(self, request): #mostrar lista de postulantes
        postulantes = Administrador.objects.all()
        return render(request, self.template_name, {"postulantes": postulantes})

