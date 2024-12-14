from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return (f'Datos del Profesor:'
                f'ID:{self.id}'
                f'Nombre:{self.nombre}'
                f'Apellido:{self.apellido}'
                f'Email:{self.apellido}'
                f'Telefono:{self.telefono}')

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(15)
    direccion = models.CharField(100)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return (f'Datos del Alumno'
                f'Id : {self.id}'
                f'Nombre:{self.nombre}'
                f'Apellido:{self.apellido}'
                f'Email:{self.email}'
                f'Telefono:{self.telefono}'
                f'Direccion:{self.direccion}'
                f'fecha_ingreso:{self.fecha_ingreso}')

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno,related_name="cursos")

    def __str__(self):
        return (f'Datos del Curso:'
                f'Nombre:{self.nombre}'
                f'Descripcion:{self.descripcion}'
                f'Fecha de Inicio:{self.fecha_inicio}'
                f'Fecha de Fin:{self.fecha_fin}'
                f'Profesor:{self.profesor}'
                f'Alumnos:{self.alumnos}')

