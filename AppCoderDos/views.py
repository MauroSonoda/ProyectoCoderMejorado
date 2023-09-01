from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
#cargo ,despues la url
def curso (req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    curso.save() #lo guarda en la base de dato
    return HttpResponse(f"el {curso.nombre} {curso.camada} creado")
def lista_cursos(req):
    #utilizo los mannger para leer de base de dato
    lista=Curso.objects.all() #devolvera todo dntro del objects estan los manager
    return render(req,"lista_cursos.html",{"lista_cursos" : lista})#el contexto