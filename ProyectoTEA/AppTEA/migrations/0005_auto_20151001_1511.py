# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0004_auto_20151001_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
    ]
