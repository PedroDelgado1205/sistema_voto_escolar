from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CURSOS = (('Primero', 1), ('Segundo', 2), ('tercero', 3), ('Cuarto', 4))
PARALELOS = ('A', 'a'), ('B', 'b'), ('C', 'c')


class Curso(models.Model):
    nivel = models.IntegerField(default=1)
    paralelo = models.CharField(max_length=1, default='a')

    def __str__(self) -> str:
        return f"Nivel {self.nivel}, Paralelo {self.paralelo}"


class Estudiante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name}, {self.curso}"
