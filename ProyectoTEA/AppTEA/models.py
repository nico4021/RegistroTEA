from django import forms
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Area(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'

class Paciente(models.Model):
    dni = models.IntegerField()
    apellidos = models.CharField(max_length=30)
    diagnostico = models.CharField(max_length=300)
    obra_social = models.CharField(max_length=20)
<<<<<<< HEAD
    foto = models.ImageField(blank=True)
=======
    foto = models.ImageField()
>>>>>>> 157196d7a1882e88e43f73a9441b23ec3beb8e8e
    fecha_nacimiento = models.DateField(blank=False)
    #numero_afiliado es un numero pero lleva guiones
    numero_afiliado = models.CharField(max_length=30)
    nombres = models.CharField(max_length=40)

    def __str__(self):
        return self.apellidos

    def edad(fecha_nacimiento):
        hoy = date.today()
        return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

class Presupuesto(models.Model):
    paciente = models.ForeignKey(Paciente)
    tratamiento_prestacion = models.CharField(max_length=50)
    #horas por semana que asiste el profesional
    horas_semanales = models.IntegerField()
    #horas por mes que asiste el profesional
    horas_mensuales = models.IntegerField()
    domicilio_prestacion = models.CharField(max_length=40)
    #costo de una hora
    costo_hora = models.IntegerField()
    #Martes, jueves, etc
    dias_semanales = models.CharField(max_length=100)
    horario = models.CharField(max_length=6)
    #Cantidad (1, 2, 18, etc) Veces por semana
    frecuencia = models.IntegerField()
    costo_mensual = models.IntegerField()

    
    class Meta:
        verbose_name = 'presupuesto'
        verbose_name_plural = 'presupuestos'

class Profesional(User):
    #Registro nacional de proveedores
    rnp = models.IntegerField()
    dni =  models.CharField(max_length=10)
    profesion = models.CharField(max_length=40)
    num_matricula = models.IntegerField()
    tel_personal = models.IntegerField()

    def __str__(self):
        return self.apellidos
        
    class Meta:
        verbose_name = 'profesional'
        verbose_name_plural = 'profesionales'

