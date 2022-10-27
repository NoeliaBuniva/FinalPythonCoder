from django.shortcuts import render, get_object_or_404
from django.views import View
from About.models import Administrador
from About.forms import AdministradorForm


# Nuestra los datos de la BD
class ListaPostulantes(View):
    template_name = "About/lista_postu.html"

    def get(self, request): #mostrar lista de postulantes
        postulantes = Administrador.objects.all()
        return render(request, self.template_name, {"postulantes": postulantes})

# Se carga modulo para agregar datos a la BD
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


# Se carga modulo para la edición de los datos de la BD
class EditPostulantes(View):
    template_name = "About/edit_postulantes.html"
    succsess_template = "About/exito.html"
    form_class = AdministradorForm
    initial = {"nombre":"", "apellido":"", "edad":"", "profesion":""}

    def get(self, request, pk):
        postulante = get_object_or_404(Administrador, pk = pk)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(Administrador, pk=pk)
        form = self.form_class(request.POST, instance=postulante)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.succsess_template)  




