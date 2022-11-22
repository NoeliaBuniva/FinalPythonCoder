"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from About.views import (horarios_detalle, home, SignUpView, DeleteRutinas, CargarRutinas, ListaRutinas, EditRutinas, ListaPostulantes, CargarPostulantes, EditPostulantes, DeletePostulantes, index, AboutUs, buscarEntrenamientos) 
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postulantes/', ListaPostulantes.as_view(), name= "lista"),
    path('postulantes/cargar/', CargarPostulantes.as_view(), name = "cargar_postu"), 
    path('postulantes/editar/<int:pk>', EditPostulantes.as_view(), name = "editar"),
    path('postulantes/delete/<int:pk>', DeletePostulantes.as_view(), name = "borrar"),
    path("inicio/", index, name="inicio"),
    path("inicio/aboutus", AboutUs, name="sobre_nosotros"),
    path('busqueda_entrenamientos/', buscarEntrenamientos.as_view(), name = "Entrenamientos"),
    path('busqueda_entrenamientos/busqueda_entrenamientos/', buscarEntrenamientos.as_view()),
    path('rutinas/', ListaRutinas.as_view(), name= "Lista Rutinas"),
    path('rutinas/cargar/', CargarRutinas.as_view(), name = "CargarRutinas"), 
    path('rutinas/editar/<int:pk>', EditRutinas.as_view(), name = "Editar"),
    path('rutinas/delete/<int:pk>', DeleteRutinas.as_view(), name = "Borrar"),
    path('logout/', LogoutView.as_view(template_name='About/logout.html'), name = 'Logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('sesión/', TemplateView.as_view(template_name='About/mensaje_login.html'), name='Sesión iniciada'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('', home, name = "home"),
    #path('<int:pk>/', horarios_detalle.as_view(), name = "horarios"),

]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
