# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha', models.DateField(default=b'1')),
                ('contenido', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'informe',
                'verbose_name_plural': 'informes',
            },
        ),
        migrations.RemoveField(
            model_name='cobranza',
            name='profesional',
        ),
        migrations.RemoveField(
            model_name='presupuesto',
            name='cobranza',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profesional',
            name='cuit',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellidos',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=15),
        ),
        migrations.RemoveField(
            model_name='presupuesto',
            name='profesional',
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='profesional',
            field=models.ForeignKey(default=1, to='AppTEA.Profesional'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profesional',
            name='dni',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='num_matricula',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='rnp',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='tel_personal',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Cobranza',
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
