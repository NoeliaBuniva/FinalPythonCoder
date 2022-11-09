from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from About.models import FichaSocio
from About.forms import FichaSocioForm

# No se para que es ésto
from this import d





def index(request): #para ir a la plantilla
    posteos = FichaSocio.objects.order_by('-date_published').all()
    return render(request, "About/index.html")


# Muestra los datos de la BD
class ListaPostulantes(View):
    template_name = "About/lista_postu.html"

    def get(self, request): #mostrar lista de postulantes
        postulantes = FichaSocio.objects.all()
        return render(request, self.template_name, {"postulantes": postulantes})

# Se carga módulo para agregar datos a la BD
class CargarPostulantes(View):
    template_name = "About/cargar_postulantes.html"
    form_class = FichaSocioForm
    initial = {"nombre":""}#, "apellido":"", "edad":""}

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
    form_class = FichaSocioForm
    initial = {"nombre":"", "apellido":"", "edad":"", "descripcion":"", "imagen01":""}

    def get(self, request, pk):
        postulante = get_object_or_404(FichaSocio, pk = pk)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(FichaSocio, pk=pk)
        form = self.form_class(request.POST, instance=postulante)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.succsess_template)  


# Se carga modulo para borrar datos de la BD
class DeletePostulantes(View):
    template_name = "About/delete_postulantes.html"
    succsess_template = "About/exito.html"
    form_class = FichaSocioForm
    initial = {"nombre":"", "apellido":"", "edad":""}

    def get(self, request, pk):
        postulante = get_object_or_404(FichaSocio, pk = pk)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(FichaSocio, pk=pk)
        postulante.delete()
        return render(request, self.succsess_template)  

#desde acá agregue yo 


def inicio(request): #todavia nada util jaja
    return render(request, "About/inicio.html")

def AboutUs(request,View): 
    return render(request, "About/about_us.html")

def eliminarPostu(request, Postu_nombre):
    Postu = FichaSocio.objects.get(nombre = Postu_nombre)
    Postu.delete()

    Postulantes = FichaSocio.objects.all()
    contexto = {"Postulantes": Postulantes}
    return render(request, "About/leerpostu.html", contexto)

class ListaPostulantes1(View): #lo mismo q la principal q habíamos hecho
    template_name = "About/leerpostu.html"

    def get(self, request): #mostrar lista de postulantes con agregar y eliminar
        Postulantes = FichaSocio.objects.all()
        return render(request, self.template_name, {"Postulantes": Postulantes})


def editarPostu(request, Postu_nombre):
    Postu = FichaSocio.objects.get(nombre = Postu_nombre)
    Postu.Update()

    Postulantes = FichaSocio.objects.all()
    contexto = {"Postulantes": Postulantes}
    return render(request, "About/leerpostu.html", contexto)



#este de aca abajo es el intento de modificacion del argumento de editar un postu, no se que hacer ahre
class EditPostulantes1(View):
    template_name = "About/edit_postulantes.html"
    succsess_template = "About/exito.html"
    form_class = FichaSocioForm
    initial = {"nombre":"", "apellido":"", "edad":"", "descripcion":"", "imagen01":""}

    def get(self, request, pk):
        Postu = FichaSocio.objects.get(nombre = Postu_nombre) #deberia decir algo con postu nombre o pk q es el arg q recibe la funcion get
        postulante = get_object_or_404(FichaSocio, pk = Administrador.nombre)
        form = self.form_class(instance = postulante)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        postulante = get_object_or_404(FichaSocio, pk= pk)
        form = self.form_class(request.POST, instance=postulante)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.succsess_template)  

@login_required
def index(request):
    return render(request, 'About/index.html')

@login_required
class ListPost(ListView):
    model=FichaSocio

@login_required
class ListPost(LoginRequiredMixin, ListView):
    model=FichaSocio

class BlogLogin(LoginView):
    template_name = 'About/login.html'
    next_page = reverse_lazy("Inicio")

class BlogLogout(LogoutView):
    template_name = 'About/logout.html'


