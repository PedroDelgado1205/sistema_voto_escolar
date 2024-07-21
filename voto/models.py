from django.db import models
from candidato.models import Candidato
from estudiante.models import Estudiante

# Create your models here.

class Voto(models.Model):
    voto_por = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    voto_de = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
