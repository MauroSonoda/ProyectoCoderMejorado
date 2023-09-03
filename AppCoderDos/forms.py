from django import forms #crear formulario desde django 
class CursoFormulario(forms.Form):
    curso=forms.CharField(required=True)
    camada=forms.IntegerField(required=True)
class ProfesorFormulario(forms.Form):
    nombre=forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()

