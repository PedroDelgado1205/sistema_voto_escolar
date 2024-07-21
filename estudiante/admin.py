from django.contrib import admin

# Register your models here.
from estudiante.models import Curso, Estudiante

modelos = [Curso, Estudiante]

admin.site.register(modelos)