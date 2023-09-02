from django.db import models
# Create your models here,para la base de dato
class Curso(models.Model):#hereda de la clase model porque de esa manera django sabe que curso es un modelo
    nombre = models.CharField(max_length=50)#attributos
    camada= models.IntegerField()
    
    def __str__(self):
        return self.nombre
#Cuando hagamos la migraciones este modelo se transforma en una tabla
#de modelo a base de dato 
# a)python manage.py makemigrations
# b)Cargo app coder  en setting            
# c) y por ultimo migro.
def __str__(req):
    return f"{Curso.nombre}"
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email=models.EmailField(null=True) #como ya tengo registro le coloco null
    def __str__(self):
        return f'{self.nombre} {self.Apellido}' #para verlos en el admin con nombres
    class meta():
        verbose_name='studients' #para cambiarle el nombre 
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email=models.EmailField(null=True)
    profesion =models.CharField(max_length=50)
    curso=models.ManyToManyField(Curso)
    def __str__(self):
        return f'{self.nombre} {self.Apellido}'
    
    # paso a views para agregar los cros
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    Estudiantes=models.ForeignKey(Estudiantes, on_delete=models.CASCADE) #MODIFICAR EL ADMIN SI ELIMINO ESTUDIANTE ELIMINO SUS ENTREGABLE 
        #recupero los datos del estudiantes por id
        
#subo todo a git hub      
#git init
# git branch -m main 
#git add .
#git commit -m 'first commit'
#copio el comando de git y lo pongo en el comp.
#git push -m origin main