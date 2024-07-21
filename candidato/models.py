from django.db import models
from estudiante.models import Estudiante


# Create your models here.

class Lista(models.Model):
    nombre = models.CharField(max_length=40)
    lema = models.TextField()
    propuestas = models.TextField()
    foto = models.ImageField(upload_to='lista')

    def __str__(self):
        return f"{self.nombre}"


class Dignidad(models.Model):
    nombre = models.CharField(max_length=40)
    funciones = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Candidato(models.Model):
    candidato = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='cadidato')
    dignidad = models.ForeignKey(Dignidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidato.user.first_name}, {self.lista.nombre}, {self.dignidad.nombre}, {self.foto}"