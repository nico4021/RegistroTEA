# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from fractions import Fraction
from decimal import Decimal


class Curso(models.Model):
    # Atributos de la clase
    numero = models.IntegerField("Curso",max_length=1)
    division = models.CharField("Division", max_length=1)
    anio = models.IntegerField("Ciclo lectivo",max_length=4)
    
    class Meta:
        ordering = ('-anio', 'numero', 'division')
    
    # Metodos de la clase
    def __unicode__(self):
        curso = str(self.numero)+" \""+str(self.division)+"\" - "+str(self.anio)
        return curso
    
# HERENCIA DE USUARIO
class Preceptor(User):
    cursos = models.ManyToManyField(Curso)
    
    class Meta:
        verbose_name = 'preceptor'
        verbose_name_plural = 'preceptores'
        
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.username
      
    def observar(self, alumno, descripcion):
        self.observacion_set.create(descripcion=descripcion)
        return descripcion

#Clase alumno:
class Alumno(User):
    # Atributos de la clase
    reincorporacion = models.IntegerField("Reincorporacion", max_length=2, default=0)
    dni = models.IntegerField("Dni", max_length=100)
    curso = models.ForeignKey(Curso)
    
    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.username
    
    # Devuelve todas las faltas del alumno
    def totalFaltas(self):
        return self.inasistencia_set.all()

    # Devuelve todas las faltas del alumno
    def faltas(self, b=False, m='anual'):
	if m == 'mensual':
	    fts = self.inasistencia_set.filter(fecha__month=datetime.now().month, fecha__year=datetime.now().year)
	elif m == 'anual':
	    fts = self.inasistencia_set.filter(fecha__year=datetime.now().year)
	else:
	    fts = self.inasistencia_set.all()

	tot = 0
	
	for i in fts:
	    tot += i.tipo
	    
	if b:
	    return tot
	else:
	    return self.a_mixto(tot)
    
class Observacion (models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=datetime.now())
    
    # relacion con el preceptor
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)

    class Meta:
        verbose_name_plural = 'observaciones'
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.descripcion + self.fecha

class Amonestacion (models.Model):
    cantidad = models.IntegerField("Cantidad",max_length=2)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(default=datetime.now())
    
    # relacion con el preceptor
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)

    class Meta:
        verbose_name_plural = 'amonestaciones'
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.cantidad + self.descripcion + self.fecha

class Inasistencia (models.Model):
    tipo = models.FloatField()
    justificado = models.BooleanField(default=False)
    fecha = models.DateField()
    preceptor = models.ForeignKey(Preceptor)
    alumno = models.ForeignKey(Alumno)
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.fecha.__str__()

    def justificar(self, bo):
	self.justificado = bo
	self.save()
	return self.justificado
    
    def cantMixto(self):
        frac = Fraction(self.tipo).__str__()
        mixto = ''

        if frac != '0':
            mixto += ''+frac

        if frac == '0' and not self.tipo:
            mixto += '0'
	
        return mixto
