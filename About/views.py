from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from About.forms import FichaSocioForm, entrenamientos_Form, rutina_Form 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.admin import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from About.models import FichaSocio, entrenamientos, rutina, horarios 


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
    initial = {"nombre":""}

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

def AboutUs(request): 
    return render(request, "About/about_us.html")

@login_required
def index(request):
    return render(request, 'About/index.html')

@login_required
class ListPost(ListView):
    model=FichaSocio

@login_required
class ListPost(LoginRequiredMixin, ListView):
    model=FichaSocio

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    return render(request, "About/home.html")

class horarios_detalle(generic.ListView):
    model = horarios
    template_name = "About/horarios_detalle.html"

    def get(self, request): #mostrar lista de horarios
        lista_horarios = horarios.objects.all()
        return render(request, self.template_name, {"horarios": lista_horarios})

class descripción_h(DetailView):
    model = horarios
    template_name = "About/descripción.html"
    
    
class buscarEntrenamientos(View):
    form_class = entrenamientos_Form 
    template_name = 'About/buscar_entrenamientos.html'
    initial = {"grupo muscular":""}

    def get(self, request):
        form = self.form_class(initial=self.initial) 
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        datos = rutina.objects.all
        if form.is_valid():
            grupo_muscular = form.cleaned_data["grupo_muscular"] 
            sexo = form.cleaned_data["sexo"] 
            form = self.form_class(initial=self.initial)
            if sexo == "F" and grupo_muscular == "TS":
                return render(request, 'About/fem_ts.html',  {"form": form, "grupo muscular": grupo_muscular, "sexo": sexo})
            elif sexo == "F"  and grupo_muscular == "TI":
                return render(request, 'About/fem_ti.html', {"form": form, "grupo muscular": grupo_muscular, "sexo": sexo})
            elif sexo == "M"  and grupo_muscular == "TS":
                return render(request, 'About/masc_ts.html', {"form": form, "grupo muscular": grupo_muscular, "sexo": sexo})
            elif sexo == "M"  and grupo_muscular == "TI":
                return render(request, 'About/masc_ti.html', {"form": form, "grupo muscular": grupo_muscular, "sexo": sexo})
            elif sexo == "M" or sexo == "F" and grupo_muscular == "C":
                return render(request, 'About/core.html', {"form": form, "grupo muscular": grupo_muscular, "sexo": sexo})
        return render(request, self.template_name, {'form':form})


class ListaRutinas(View):
    template_name = "About/rutinas.html"

    def get(self, request): #mostrar lista de rutinas
        rutinas = rutina.objects.all()
        return render(request, self.template_name, {"rutinas": rutinas})
    
class CargarRutinas(View):
    template_name = "About/cargar_rutinas.html"
    form_class = rutina_Form
    initial = {"ejercicios":""}

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
class EditRutinas(View):
    template_name = "About/edit_rutinas.html"
    success_template = "About/exito.html"
    form_class = rutina_Form
    initial = {"ejercicios":""}

    def get(self, request, pk):
        rutinas = get_object_or_404(rutina, pk = pk)
        form = self.form_class(instance = rutinas)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        rutinas = get_object_or_404(rutina, pk=pk)
        form = self.form_class(request.POST, instance=rutinas)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.success_template) 

# Se carga modulo para borrar datos de la BD
class DeleteRutinas(View):
    template_name = "About/delete_rutinas.html"
    success_template = "About/exito.html"
    form_class = rutina_Form
    initial = {"ejercicios":""}

    def get(self, request, pk):
        rutinas = get_object_or_404(rutina, pk = pk)
        form = self.form_class(instance = rutinas)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        rutinas = get_object_or_404(rutina, pk=pk)
        rutinas.delete()
        return render(request, self.success_template) 