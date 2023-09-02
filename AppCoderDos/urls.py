from django.urls import path
from AppCoderDos.views import curso,lista_cursos,profesores,entregables,inicio,estudiantes,cursos
urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('profesores/', profesores,name='profesores'),
    path('entregables/', entregables,name='entregables'),
    path('', inicio,name='inicio'),
    path('estudiantes/', estudiantes,name='estudiantes'),
    path('cursos/', cursos,name='cursos'),#para otro hrf
]
 