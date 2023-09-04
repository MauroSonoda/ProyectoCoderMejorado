from django.urls import path
from AppCoderDos.views import *
urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('profesores/', profesores,name='profesores'),
    path('entregables/', entregables,name='entregables'),
    path('', inicio,name='inicio'),
    path('estudiantes/', estudiantes,name='estudiantes'),
    path('cursos/', cursos,name='cursos'),#para otro hrf
    path('curso-formulario/',cursoformulario,name='cursoformulario'),
    path('busqueda-camada/',busquedaCamada,name='busquedaCamada'),
    path('buscar/',buscar,name='buscar'),
    path('lista-estudiantes/',listaEstudiantes,name='listaestudiantes'),
    path('lista-profesores/',listaProfesores,name='listaProfesores'),
    path('crea-profesor/',CreaProfesores,name="creaprofesor"),
    path('eliminaProfesor/<int:id>',eliminarProfesor,name="eliminaprofesor"),   
]