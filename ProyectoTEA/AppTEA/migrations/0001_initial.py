# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
<<<<<<< HEAD
from django.conf import settings
import django.contrib.auth.models
=======
import datetime
import django.contrib.auth.models
from django.conf import settings
>>>>>>> 0bd7b3504a6b1ebec30ee17b8e1c3dd0dc269046


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
<<<<<<< HEAD
                ('fecha', models.DateField(default=b'1')),
=======
                ('fecha', models.DateField(default=datetime.datetime.now)),
>>>>>>> 0bd7b3504a6b1ebec30ee17b8e1c3dd0dc269046
                ('contenido', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'informe',
                'verbose_name_plural': 'informes',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=15)),
                ('obra_social', models.CharField(max_length=20)),
                ('numero_afiliado', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('diagnostico', models.CharField(max_length=300)),
                ('foto', models.ImageField(upload_to=b'profile_images', blank=True)),
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
                ('is_active', models.BooleanField(default=True)),
                ('tratamiento_prestacion', models.CharField(max_length=50)),
                ('horas_semanales', models.IntegerField()),
                ('horas_mensuales', models.IntegerField()),
                ('domicilio_prestacion', models.CharField(max_length=40)),
                ('costo_hora', models.IntegerField()),
                ('dias_semanales', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=6)),
                ('frecuencia', models.IntegerField()),
                ('costo_mensual', models.IntegerField()),
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
                ('rnp', models.CharField(max_length=15)),
                ('dni', models.CharField(max_length=15)),
                ('num_matricula', models.CharField(max_length=15)),
                ('tel_personal', models.CharField(max_length=20)),
                ('cuit', models.CharField(max_length=20)),
                ('area', models.ForeignKey(to='AppTEA.Area')),
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
        migrations.AddField(
            model_name='presupuesto',
            name='profesional',
            field=models.ForeignKey(to='AppTEA.Profesional'),
        ),
        migrations.AddField(
            model_name='informe',
            name='paciente',
            field=models.ForeignKey(to='AppTEA.Paciente'),
        ),
        migrations.AddField(
            model_name='informe',
            name='profesional',
            field=models.ForeignKey(to='AppTEA.Profesional'),
        ),
    ]
