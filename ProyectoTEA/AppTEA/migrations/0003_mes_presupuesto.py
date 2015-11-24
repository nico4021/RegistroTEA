# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0002_auto_20151117_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mes_presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.DateField(default=datetime.datetime.now)),
                ('dinero_total', models.IntegerField(blank=True)),
                ('profesional', models.ForeignKey(to='AppTEA.Profesional')),
            ],
        ),
    ]
