from django import forms
from About.models import FichaSocio, entrenamientos, rutina 

class FichaSocioForm(forms.ModelForm):
    class Meta:
        model = FichaSocio
        fields = ['nombre', 'apellido', 'edad', 'descripcion','imagen01']

class entrenamientos_Form(forms.ModelForm):
    class Meta:
        model = entrenamientos 
        fields = ['grupo_muscular', 'sexo']

class rutina_Form(forms.ModelForm):
    class Meta:
        model = rutina
        fields = ['ejercicios']