from django import forms
from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone


"""
Modelo de area
"""
class Area(models.Model):
    # Atributos
    is_active = models.BooleanField(default=True)

    nombre = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'


"""
Modelo de profesional

:Usuario: Usuario del sistema, hereda del modelo User
:RNP: Registro nacional de proveedores
"""
class Profesional(User):
    # Relaciones
    area = models.ForeignKey(Area)

    # Atributos
    rnp = models.CharField(max_length=15)
    dni =  models.CharField(max_length=15)
    num_matricula = models.CharField(max_length=15)
    tel_personal = models.CharField(max_length=20)
    cuit = models.CharField(max_length=20)

    def __unicode__(self):
        return self.first_name + " " + self.last_name
        
    class Meta:
        verbose_name = 'profesional'
        verbose_name_plural = 'profesionales'


"""
Modelo de paciente
"""
class Paciente(models.Model):
    # Atributos
    is_active = models.BooleanField(default=True)

    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    dni = models.CharField(max_length=15)
    obra_social = models.CharField(max_length=20)
    numero_afiliado = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank=False)
    diagnostico = models.CharField(max_length=300)
    foto = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.nombres + " " + self.apellidos

    def edad(fecha_nacimiento):
        hoy = date.today()
        return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'



"""
Modelo de informe
"""
class Informe(models.Model):
    # Relaciones
    paciente = models.ForeignKey(Paciente)
    profesional = models.ForeignKey(Profesional)

    # Atributos
    is_active = models.BooleanField(default=True)

    fecha = models.DateField(blank=False, default=timezone.now)
    contenido = models.CharField(max_length=400)
    
    def __unicode__(self):
        return "Informe de "+self.paciente.nombres+" del "+self.fecha.strftime("%d/%m/%Y")
    
    class Meta:
        verbose_name = 'informe'
        verbose_name_plural = 'informes'


"""
Modelo de presupuesto
"""
class Presupuesto(models.Model):
    # Relaciones
    paciente = models.ForeignKey(Paciente)
    profesional = models.ForeignKey(Profesional)
    
    # Atributos
    is_active = models.BooleanField(default=True)

    tratamiento_prestacion = models.CharField(max_length=50)
    domicilio_prestacion = models.CharField(max_length=40)
    #costo de una hora
    costo_hora = models.IntegerField()
    costo_mensual = models.IntegerField()
    #Fecha en que se genera el presupuesto
    fecha_creacion = models.DateField(default=datetime.now)
    def __unicode__(self):
        return self.paciente.nombres+" "+self.paciente.apellidos+" "+self.fecha_creacion.strftime("%d/%m/%Y")
    
    class Meta:
        verbose_name = 'presupuesto'
        verbose_name_plural = 'presupuestos'
        
"""
Modelo de un Horario, necesario para poder crear un presupueso
# Dia #Hora de entrada #Hora de salida
"""        
class Horario(models.Model):
    #Relaciones
    presupuesto = models.ForeignKey(Presupuesto)
    
    #Atributos
    dia = models.CharField(max_length=7)
    hora_entrada = models.CharField(max_length = 20)
    hora_salida = models.CharField(max_length = 20)
    cantidad_horas = models.IntegerField(blank=True)
    def __unicode__(self):
        return self.dia+" de "+self.hora_entrada+" a "+self.hora_salida