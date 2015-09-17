# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(max_length=9)),
                ('apellidos', models.CharField(max_length=30)),
                ('diagnostico', models.CharField(max_length=300)),
                ('obra_social', models.CharField(max_length=20)),
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
                ('horas_semanales', models.IntegerField(max_length=2)),
                ('horas_mensuales', models.IntegerField(max_length=3)),
                ('domicilio_prestacion', models.CharField(max_length=40)),
                ('costo_hora', models.IntegerField(max_length=5)),
                ('dias_semanales', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=6)),
                ('frecuencia', models.IntegerField(max_length=5)),
                ('costo_mensual', models.IntegerField(max_length=20)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rnp', models.IntegerField(max_length=8)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=10)),
                ('profesion', models.CharField(max_length=40)),
                ('num_matricula', models.IntegerField(max_length=20)),
                ('tel_personal', models.IntegerField(max_length=40)),
            ],
            options={
                'verbose_name': 'profesional',
                'verbose_name_plural': 'profesionales',
            },
        ),
    ]
