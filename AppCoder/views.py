from django.shortcuts import render
from AppCoder.models import Tarea

def mostrar_mi_template(request, nombre, apellido):
    context = {
        "nombre" : nombre,
        "apellido" : apellido,
        "notas": [5,6,7,8,9,10]
    }
    return render(request, "AppCoder/index.html", context)

def mostrar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request,"AppCoder/tareas.html",{"tareas":tareas})