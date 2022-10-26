from django import forms
from About.models import Administrador

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'apellido', 'edad', 'profesion']
        