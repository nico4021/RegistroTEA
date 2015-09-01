from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


#Le agrego area al profesional.
#class Profesional(User):
#    area = models.ManyToManyField(Area)
#
# Lo comente porque me tiraba error, Area no esta definido
#

class Area(models.Model):
    nombre = models.CharField(max_length=40)
    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'

# class Paciente(models.Model):
#     dni
#     apellidos
#     diagnostico
#     obra_social
