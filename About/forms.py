from django import forms
from About.models import FichaSocio

class FichaSocioForm(forms.ModelForm):
    class Meta:
        model = FichaSocio
        fields = ['nombre', 'apellido', 'edad']
        