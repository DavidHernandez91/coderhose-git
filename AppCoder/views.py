from django.shortcuts import render
from AppCoder.models import Tarea,Persona

def mostrar_mi_template(request, nombre, apellido):
    context = {
        "nombre" : nombre,
        "apellido" : apellido,
        "notas": [5,6,7,8,9,10]
    }
    return render(request, "AppCoder/index.html", context)

def mostrar_tareas(request,criterio):
        if criterio == "todo":
            tareas = Tarea.objects.all()
        elif criterio:
            tarea = Tarea.objects.filter(nombre=criterio).all()
        return render(request,"AppCoder/tareas.html",{"tareas":tareas})

def mostrar_personas(request):
        personas = Persona.objects.all()
        total_personas = len(personas)
        return render(request,"AppCoder/personas.html",{"personas":personas,"total_personas":total_personas})