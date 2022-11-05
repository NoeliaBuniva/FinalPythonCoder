from this import d
from django.shortcuts import render, get_object_or_404
from django.views import View
from About.models import Administrador
from About.forms import AdministradorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from About.models import Administrador
from django.urls import reverse_lazy


# Muestra los datos de la BD
class ListaPostulantes(View):
    template_name = "About/lista_postu.html"

    def get(self, request): #mostrar lista de postulantes
        postulantes = Administrador.objects.all()
        return render(request, self.template_name, {"postulantes": postulantes})

# Se carga módulo para agregar datos a la BD
class CargarPostulantes(View):
    template_name = "About/cargar_postulantes.html"
    form_class = AdministradorForm
    initial = {"nombre":""}#, "apellido":"", "edad":"", "profesion":""}

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


# Se carga modulo para borrar datos de la BD
class DeletePostulantes(View):
    template_name = "About/delete_postulantes.html"
    succsess_template = "About/exito.html"
    form_class = AdministradorForm
    initial = {"nombre":"", "apellido":"", "edad":"", "profesion":""}

    def get(self, request, pk):
        postulante = get_object_or_404(Administrador, pk = pk)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(Administrador, pk=pk)
        postulante.delete()
        return render(request, self.succsess_template)  

#desde acá agregue yo 
def index(request): #para ir a la plantilla
    return render(request, "About/index.html")

def inicio(request): #todavia nada util jaja
    return render(request, "About/inicio.html")

def AboutUs(request): 
    return render(request, "About/about_us.html")

def eliminarPostu(request, Postu_nombre):
    Postu = Administrador.objects.get(nombre = Postu_nombre)
    Postu.delete()

    Postulantes = Administrador.objects.all()
    contexto = {"Postulantes": Postulantes}
    return render(request, "About/leerpostu.html", contexto)

class ListaPostulantes1(View): #lo mismo q la principal q habíamos hecho
    template_name = "About/leerpostu.html"

    def get(self, request): #mostrar lista de postulantes con agregar y eliminar
        Postulantes = Administrador.objects.all()
        return render(request, self.template_name, {"Postulantes": Postulantes})


def editarPostu(request, Postu_nombre):
    Postu = Administrador.objects.get(nombre = Postu_nombre)
    Postu.Update()

    Postulantes = Administrador.objects.all()
    contexto = {"Postulantes": Postulantes}
    return render(request, "About/leerpostu.html", contexto)



#este de aca abajo es el intento de modificacion del argumento de editar un postu, no se que hacer ahre
class EditPostulantes1(View):
    template_name = "About/edit_postulantes.html"
    succsess_template = "About/exito.html"
    form_class = AdministradorForm
    initial = {"nombre":"", "apellido":"", "edad":"", "profesion":""}

    def get(self, request, pk):
        Postu = Administrador.objects.get(nombre = Postu_nombre) #deberia decir algo con postu nombre o pk q es el arg q recibe la funcion get
        postulante = get_object_or_404(Administrador, pk = Administrador.nombre)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(Administrador, pk= pk)
        form = self.form_class(request.POST, instance=postulante)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.succsess_template)  

@login_required
def index(request):
    return render(request, 'About/index.html')

class ListPost(ListView):
    model=Administrador

class ListPost(LoginRequiredMixin, ListView):
    model=Administrador

class BlogLogin(LoginView):
    template_name = 'inicio/login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'inicio/logout.html'


