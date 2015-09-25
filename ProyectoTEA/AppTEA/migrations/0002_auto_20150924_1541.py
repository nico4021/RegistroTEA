# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.auth.models
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppTEA', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profesional',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='profesional',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='profesional',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profesional',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='profesional',
            name='nombres',
        ),
        migrations.AddField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
        migrations.AddField(
            model_name='profesional',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=datetime.datetime(2015, 9, 24, 18, 41, 37, 589000, tzinfo=utc), serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='costo_hora',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='costo_mensual',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='frecuencia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='horas_mensuales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='horas_semanales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='num_matricula',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='rnp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='tel_personal',
            field=models.IntegerField(),
        ),
    ]
