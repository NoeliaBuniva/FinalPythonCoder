from django import forms
from About.models import entrenamientos, rutina, horarios, recetas
from django.contrib.auth.forms import UserCreationForm

        
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
    

class horarios_form(forms.ModelForm):
    class Meta:
        model = horarios
        fields = ['día', 'sede', 'horario', 'clase']


class recetas_form(forms.ModelForm):
    class Meta:
        model = recetas
        fields = ['comida', 'ingredientes', 'preparación', 'receta_imagen']