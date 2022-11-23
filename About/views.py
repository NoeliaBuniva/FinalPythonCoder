from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from About.forms import UpdateUserForm, entrenamientos_Form, rutina_Form, recetas_form 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from django.views.generic import DetailView
from About.models import rutina, horarios, recetas
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


# Se carga modulo para la edición de los datos de la BD
class EditRecetas(View):
    template_name = "About/edit_recetas.html"
    success_template = "About/exito.html"
    form_class = recetas_form
    initial = {"comida":"", "ingredientes":"", "preparación":"", "receta_imagen":""}

    def get(self, request, pk):
        receta = get_object_or_404(recetas, pk = pk)
        form = self.form_class(instance = receta)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        receta = get_object_or_404(recetas, pk=pk)
        receta_objetos = recetas.objects.all()
        form = self.form_class(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            form=self.form_class(initial=self.initial)
        return render(request, self.success_template, {"receta_objetos": receta_objetos})  


# Se carga modulo para borrar datos de la BD
class DeleteRecetas(View):
    template_name = "About/delete_recetas.html"
    success_template = "About/exito.html"
    form_class = recetas_form
    initial = {"comida":""}

    def get(self, request, pk):
        receta = get_object_or_404(recetas, pk = pk)
        form = self.form_class(instance = receta)
        return render(request, self.template_name, {"form": form, "pk": pk})

    def post(self, request, pk):
        receta = get_object_or_404(recetas, pk=pk)
        receta.delete()
        return render(request, self.success_template)  


def AboutUs(request): 
    return render(request, "About/about_us.html")

@login_required
def index(request):
    return render(request, 'About/index.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

#@login_required
#class profile(View):

   # def get(self, request):
     #   user_form = UpdateUserForm(instance=request.user)   
     #   return render(request, 'registration/profile.html', {'user_form': user_form})

    #def post(self, request):
      #  user_form = UpdateUserForm(request.POST, instance=request.user)
       # if user_form.is_valid():
        #    user_form.save()
         #   messages.success(request, '¡Tu perfil se ha actualizado correctamente!')
          #  return redirect(to='users-profile')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            return render(request, 'registration/message.html', {'user_form': user_form})
        
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'registration/profile.html', {'user_form': user_form})

class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('modificado')

def message(request):
    return render(request, "registration/message.html")

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
    

class Receta_Imagen(View):
    template_name = "About/recetas.html"
    form_class = recetas_form

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hecho') 
        return render(request, self.template_name, {'form':form})

def success(request):
    return render(request, "About/hecho.html")

class recetas_lista(generic.ListView):
    model = recetas
    template_name = "About/recetas_lista.html"

    def get(self, request): #mostrar lista de recetas
        lista_recetas = recetas.objects.all()
        return render(request, self.template_name, {"recetas": lista_recetas})

class descripción_r(DetailView):
    model = recetas
    template_name = "About/descripción_r.html"

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