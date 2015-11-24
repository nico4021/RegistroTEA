# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0003_mes_presupuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mes_presupuesto',
            name='porcentaje_aporte',
            field=models.IntegerField(default=20, blank=True),
            preserve_default=False,
        ),
    ]
