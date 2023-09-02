from django.shortcuts import render
from .models import Curso,Estudiantes,Profesor
from django.http import HttpResponse,HttpRequest
from .forms import CursoFormulario,ProfesorFormulario

#cargo ,despues la url
def curso (req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    curso.save() #lo guarda en la base de dato
    return HttpResponse(f"el {curso.nombre} {curso.camada} creado")
def lista_cursos(req):
    #utilizo los mannger para leer de base de dato
    lista=Curso.objects.all() #devolvera todo dntro del objects estan los manager
    return render(req,"lista_cursos.html",{"lista_cursos" : lista})#el contexto
def inicio (req):
    return render(req,"inicio.html")
def cursos (req):
    return render(req,"cursos.html")
def profesores (req):
    return render(req,"profesores.html")
def estudiantes (req):
    return render(req,"estudiantes.html")
def entregables (req):
    return render(req,"entregables.html")
def cursoformulario(req:HttpRequest): #creo mi primer formulario
    print('method',req.method)
    print('post',req.POST) #el post es para hacer modificacion
    if req.method == 'POST':
        miFormulario=CursoFormulario(req.POST) 
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            curso=Curso (nombre=data["curso"],camada=data["camada"])
            curso.save()
            return render(req,"inicio.html",{"mensaje":"curso creado con exito"}) 
        else:
              return render(req,"inicio.html",{"mensaje":"formulario invalido"}) 
    else:      
        miFormulario=CursoFormulario() #creo la instancia vacia
        return render(req,"cursoformulario.html",{"miFormulario":miFormulario})
def busquedaCamada(req):
     return render(req,"busquedaCamada.html")
def buscar(req):
    if req.GET["camada"]:
        camada=req.GET["camada"] 
        curso= Curso.objects.get(camada=camada)
        return render(req,"resultadobusqueda.html",{"curso":curso})
    else:
        return HttpResponse('no escribistre ninguna camada')
def listaEstudiantes(req): #para leer todos los estudiantes
    estudiantes=Estudiantes.objects.all() #me traigo todos
    return render(req,"leerEstudiantes.html",{"estudiantes":estudiantes})
def listaProfesores(req): #para leer todos los estudiantes
    profesores=Profesor.objects.all() #me traigo todos
    return render(req,"leerProfesores.html",{"profesores":profesores})
def creaProfesor(req):
    print('method',req.method)
    print('post',req.POST) #el post es para hacer modificacion
    if req.method == 'POST':
        miFormulario=ProfesorFormulario(req.POST)
        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            profe=Profesor(nombre=data["nombre"],profesion=data["profesion"],email=data["email"])
            profe.save()
            return render(req,"inicio.html",{"mensaje":"profesor creado con exito"}) 
        else:
              return render(req,"inicio.html",{"mensaje":"formulario invalido"}) 
    else:      
        miFormulario=ProfesorFormulario() #creo la instancia vacia
        return render(req,"profesorformulario.html",{"miFormulario":miFormulario})
def elminarEstudiante(req, id):
    if req.method =='POST':
        alumno=Estudiantes.objects.get(id = id )
        alumno.delete()
        
        alumnos=Estudiantes.objects.all() #me traigo todos
    return render(req,"leerEstudiantes.html",{"alumno":alumnos})
        