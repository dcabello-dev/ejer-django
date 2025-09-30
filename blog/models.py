from django.db import models

# Create your models here.
from django.db import models

class Persona(models.Model):
    name = models.CharField(max_length=100)
    face_encoding = models.TextField()  # Almacenaremos la codificación facial como string

    def __str__(self):
        return self.name

class asistencia(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    dia = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person.name} - {self.date} {self.time}'
    