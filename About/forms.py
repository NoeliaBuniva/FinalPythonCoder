from django import forms
from About.models import FichaSocio, entrenamientos, rutina 
#from About.views import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User 

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
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Introduzca una contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = FichaSocio
        fields = ['nombre', 'email', 'password1', 'password2'] 
