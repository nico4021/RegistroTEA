# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from AppTEA.models import *


class Command(BaseCommand):
    help = 'Agrega los grupos usados con sus permisos correspondientes'

    def handle(self, *args, **options):
        # Creo el grupo profesional si no esta creado
        prof, p_created = Group.objects.get_or_create(name='profesional')

        if p_created:
            print "Grupo profesional creado."
        
        p, p_c = Permission.objects.get_or_create(codename='facturacion',
                                name='Acceso a facturacion',
                                content_type=ContentType.objects.get(app_label='AppTEA', model='Paciente'))
        if p_c:
            print "Permiso facturacion creado."

        prof.permissions.add(p)
        print "Permiso facturacion agregado."

        otros = ['add_informe', 'change_informe', 'delete_informe', 'add_presupuesto', 'change_presupuesto', 'delete_presupuesto']

        for o in otros:
            prof.permissions.add(Permission.objects.get(codename=o))
            print "Permiso {} agregado al grupo profesional.".format(o)