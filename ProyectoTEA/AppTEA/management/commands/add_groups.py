# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from AppTEA.models import *


class Command(BaseCommand):
    help = 'Agrega los grupos usados con sus permisos correspondientes'

    def handle(self, *args, **options):
        # Creo los grupos admin y profesional si no estan creados
        adm, a_created = Group.objects.get_or_create(name='admin')
        prof, p_created = Group.objects.get_or_create(name='profesional')

        if a_created:
            print "Grupo admin creado."
            perms = {
                'cname': ['areas', 'profesionales'],
                'model': ['Area', 'Profesional'],
            }

            for i in range(len(perms['cname'])):
                p, p_c = Permission.objects.get_or_create(codename=perms['cname'][i],
                                       name='Manejo total de ' + perms['cname'][i],
                                       content_type=ContentType.objects.get(app_label='AppTEA', model=perms['model'][i]))
                if p_c:
                    adm.permissions.add(p)
                    print "Permiso {} creado y agregado al grupo admin.".format(perms['cname'][i])

        otros = ['add_paciente', 'change_paciente', 'delete_paciente']

        for o in otros:
            adm.permissions.add(Permission.objects.get(codename=o))
            print "Permiso {} agregado al grupo admin.".format(o)

        if p_created:
            print "Grupo profesional creado."
            p, p_c = Permission.objects.get_or_create(codename='facturacion',
                                   name='Acceso a facturacion',
                                   content_type=None)
            if p_c:
                prof.permissions.add(p)
                print "Permiso facturacion creado y agregado."

        otros = ['add_informe', 'change_informe', 'delete_informe', 'add_presupuesto', 'change_presupuesto', 'delete_presupuesto']

        for o in otros:
            prof.permissions.add(Permission.objects.get(codename=o))
            print "Permiso {} agregado al grupo admin.".format(o)