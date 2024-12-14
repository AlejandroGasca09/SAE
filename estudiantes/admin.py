from django.contrib import admin

from estudiantes.models import Profesor, Alumno, Materia

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Materia)
