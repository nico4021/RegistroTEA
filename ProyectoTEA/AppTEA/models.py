# -*- coding: utf-8 -*-

from django import forms
from django.db import models
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone


class Area(models.Model):
    """Modelo de área.

    :var is_active: indica si esta activo o no
    :vartype is_active: BooleanField
    :var nombre: nombre del área
    :vartype nombre: CharField

    :func __unicode__:
    """

    # Atributos
    is_active = models.BooleanField(default=True)

    nombre = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'area'
        verbose_name_plural = 'areas'


class Profesional(User):
    """Modelo de profesional.

    Hereda del modelo :py:class:User. Es un usuario del sistema.

    :var area: relación con el modelo área
    :vartype area: ForeignKey
    :var rnp: Registro Nacional de Proveedores
    :vartype rnp: CharField
    :var dni: Documento Nacional de Identidad
    :vartype dni: CharField
    :var num_matricula: número de matrícula
    :vartype num_matricula: CharField
    :var tel_personal: teléfono personal
    :vartype tel_personal: CharField
    :var cuit: número de CUIT (Código Único de Identificación Tributaria)
    :vartype cuit: CharField
    """

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


class Paciente(models.Model):
    """Modelo de paciente.

    :var is_active: indica si esta activo o no
    :vartype is_active: BooleanField
    :var nombres: nombres del paciente
    :vartype nombres: CharField
    :var apellidos: apellidos del paciente
    :vartype apellidos: CharField
    :var dni: Documento Nacional de Identidad
    :vartype dni: CharField
    :var obra_social: obra social del paciente
    :vartype obra_social: CharField
    :var numero_afiliado: número de afiliado a la obra social
    :vartype numero_afiliado: CharField
    :var fecha_nacimiento: fecha de nacimiento
    :vartype fecha_nacimiento: DateField
    :var diagnostico: diagnóstico del paciente
    :vartype diagnostico: CharField
    :var foto: foto del paciente
    :vartype foto: ImageField
    """

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

    def ape_nom(self):
        return self.apellidos + ", " + self.nombres

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
    periodo = models.CharField(max_length=50)
    
    texto = models.CharField(max_length=4000)
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


class Mes_presupuesto(models.Model):
    #relaciones
    profesional = models.ForeignKey(Profesional)
    
    #Atributos
    mes = models.DateField(default = datetime.now)
    dinero_total = models.IntegerField(blank=True)
    porcentaje_aporte = models.IntegerField(blank=True)
    
    def __unicode__(self):
        return self.profesional.first_name+" "+self.mes.strftime("%m %Y")
        
    def aporte(self):
        return (self.dinero_total*self.porcentaje_aporte)/100
    
    def ganancia(self):
        return self.dinero_total-(self.dinero_total*self.porcentaje_aporte)/100