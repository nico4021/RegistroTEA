# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
<<<<<<< HEAD
                ('is_active', models.BooleanField(default=True)),
=======
>>>>>>> b8f8c62ccb8e0b6bdb02c9d6edc25af1a8b3aaa3
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Cobranza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje_aporte', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> b8f8c62ccb8e0b6bdb02c9d6edc25af1a8b3aaa3
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('apellidos', models.CharField(max_length=30)),
                ('diagnostico', models.CharField(max_length=300)),
                ('obra_social', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_afiliado', models.CharField(max_length=30)),
                ('nombres', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tratamiento_prestacion', models.CharField(max_length=50)),
                ('horas_semanales', models.IntegerField()),
                ('horas_mensuales', models.IntegerField()),
                ('domicilio_prestacion', models.CharField(max_length=40)),
                ('costo_hora', models.IntegerField()),
                ('dias_semanales', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=6)),
                ('frecuencia', models.IntegerField()),
                ('costo_mensual', models.IntegerField()),
<<<<<<< HEAD
                ('cobranza', models.ManyToManyField(to='AppTEA.Cobranza')),
=======
>>>>>>> b8f8c62ccb8e0b6bdb02c9d6edc25af1a8b3aaa3
                ('paciente', models.ForeignKey(to='AppTEA.Paciente')),
            ],
            options={
                'verbose_name': 'presupuesto',
                'verbose_name_plural': 'presupuestos',
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rnp', models.IntegerField()),
                ('dni', models.CharField(max_length=10)),
<<<<<<< HEAD
                ('num_matricula', models.IntegerField()),
                ('tel_personal', models.IntegerField()),
                ('area', models.ForeignKey(to='AppTEA.Area')),
=======
                ('profesion', models.CharField(max_length=40)),
                ('num_matricula', models.IntegerField()),
                ('tel_personal', models.IntegerField()),
>>>>>>> b8f8c62ccb8e0b6bdb02c9d6edc25af1a8b3aaa3
            ],
            options={
                'verbose_name': 'profesional',
                'verbose_name_plural': 'profesionales',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
<<<<<<< HEAD
        migrations.AddField(
            model_name='presupuesto',
            name='profesional',
            field=models.ManyToManyField(to='AppTEA.Profesional'),
        ),
        migrations.AddField(
            model_name='cobranza',
            name='profesional',
            field=models.ForeignKey(to='AppTEA.Profesional'),
        ),
=======
>>>>>>> b8f8c62ccb8e0b6bdb02c9d6edc25af1a8b3aaa3
    ]
