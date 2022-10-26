from django.shortcuts import render
from django.views import View
from About.models import Administrador
from About.forms import AdministradorForm

class ListaPostulantes(View):
    template_name = "About/lista_postu.html"

    def get(self, request): #mostrar lista de postulantes
        postulantes = Administrador.objects.all()
        return render(request, self.template_name, {"postulantes": postulantes})

class CargarPostulantes(View):
    template_name = "About/cargar_postulantes.html"
    form_class = AdministradorForm
    initial = {"nombre":"", "apellido":"", "edad":"", "profesion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})  





