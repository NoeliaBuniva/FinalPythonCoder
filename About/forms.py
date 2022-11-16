from django import forms
from About.models import Administrador, entrenamientos, rutina 

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'apellido', 'edad', 'profesion']

class entrenamientos_Form(forms.ModelForm):
    class Meta:
        model = entrenamientos 
        fields = ['grupo_muscular', 'sexo']

class rutina_Form(forms.ModelForm):
    class Meta:
        model = rutina
        fields = ['ejercicios']