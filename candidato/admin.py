from django.contrib import admin

# Register your models here.
from candidato.models import *

modelos = [Lista, Dignidad, Candidato]

admin.site.register(modelos)
