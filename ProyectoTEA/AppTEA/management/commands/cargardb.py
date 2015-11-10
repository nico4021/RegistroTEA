# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from AppTEA.models import *


class Command(BaseCommand):
    help = 'Carga la base de datos con modelos ejemplo'

    def handle(self, *args, **options):
        pacientes = {
                "dni": [40030047, 23423423, 40234443],
                "nombres": ["Luciano Leon", "Alberto", "Walle"],
                "apellidos": ["Castillo", "Juarez", u"Ludueña"],
                "diagnostico": ["Autismo", "Autismo", "Autismo"],
                "obra_social": ["CPCE", "Medife", "Robot"],
                "foto": ["profile_images/IMG_20150920_140126.jpg", "profile_images/soldando.png", ""],
                "fecha_nacimiento": ["1997-2-22", "1990-2-2", "2000-2-2"],
                "numero_afiliado": ["0001", "0002", "0003"],
            }
        areas = ["Fonoaudiologia", "Psicologia", "Psicopedagogia", "Psicomotricidad"]

        for a in areas:
            if not Area.objects.filter(nombre=a):
                Area.objects.create(nombre=a)
                print "Area {} creada.".format(a)
            else:
                print "Area {} existente.".format(a)

        for p in range(len(pacientes["dni"])):
            if not Paciente.objects.filter(dni=pacientes["dni"][p]):
                Paciente.objects.create(dni=pacientes["dni"][p], nombres=pacientes["nombres"][p], apellidos=pacientes["apellidos"][p], diagnostico=pacientes["diagnostico"][p], obra_social=pacientes["obra_social"][p], foto=pacientes["foto"][p], fecha_nacimiento=pacientes["fecha_nacimiento"][p], numero_afiliado=pacientes["numero_afiliado"][p])
                print "Paciente {} creado.".format(pacientes["nombres"][p])
            else:
                print "Paciente {} existente.".format(pacientes["nombres"][p])





        
