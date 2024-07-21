from django.contrib import admin
from voto.models import *
# Register your models here.

modelos = [Voto]

admin.site.register(modelos)
