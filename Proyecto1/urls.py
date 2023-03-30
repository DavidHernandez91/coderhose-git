"""Proyecto1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from AppCoder.views import mostrar_mi_template
from AppCoder.views import mostrar_tareas, mostrar_personas,cargar_personas,BuscarPersonas
from SocialTravel.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-template/<nombre>/<apellido>',mostrar_mi_template),
    path('mis-tareas/<criterio>',mostrar_tareas, name="tareas"),
    path('',index),
    path('personas/',mostrar_personas, name="personas"),
    path('personas/create',cargar_personas, name="personas-create"),
    path('personas/list',BuscarPersonas.as_view() ,name="personas-list")
]

