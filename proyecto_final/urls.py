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
from About.views import (EditPostulantes1, ListaPostulantes, CargarPostulantes, EditPostulantes, DeletePostulantes, index, inicio, eliminarPostu, ListaPostulantes1, AboutUs, BlogLogin, 
BlogLogout)
# from FinalPythonCoder.About.views import EditPostulantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postulantes/', ListaPostulantes.as_view(), name= "lista"),
    path('postulantes/editar/postulantes/', ListaPostulantes.as_view()),
    path('postulantes/delete/postulantes/', ListaPostulantes.as_view()),
    path('postulantes/cargar/postulantes/', ListaPostulantes.as_view()),
    path('postulantes/cargar/', CargarPostulantes.as_view(), name = "cargar_postu"), 
    path('postulantes/editar', EditPostulantes.as_view()),
    path('postulantes/editar/<int:pk>', EditPostulantes.as_view(), name = "editar"),
    path('postulantes/delete/<int:pk>', DeletePostulantes.as_view(), name = "borrar"),
    path("inicio/", index, name="inicio"), #desde acá agregué yo, este es para la plantilla
    path("página_inicio/", inicio), #este nada
    path("postulantes1/", ListaPostulantes1.as_view()), #este es el referido a leer.postu donde se podria usar los botones
    path("postulantes1/postulantes/cargar", CargarPostulantes.as_view()), #este y el de abajo = ruta lista + cargar, editar 
   # path("editarpostu/<int:pk>", EditPostulantes.as_view(), name = "EditarPostu"), #no se q arg deberia recibir para funcionar, no es ni pk ni postunombre
    path('eliminarpostu/<Postu_nombre>/', eliminarPostu, name="eliminar_postu"), #este se aplica solo cuando tocamos el boton de eliminar
    path("inicio/aboutus", AboutUs, name="sobre_nosotros"),
    path('login/', BlogLogin.as_view(), name="about_login"),
    path('logout/', BlogLogout.as_view(), name="about_logout"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
