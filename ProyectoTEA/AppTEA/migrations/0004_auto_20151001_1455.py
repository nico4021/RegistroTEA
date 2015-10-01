# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0003_auto_20151001_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'profile_images', blank=True),
        ),
    ]
