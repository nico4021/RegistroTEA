# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0002_auto_20150924_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(default=b'', null=True, upload_to=b'profile_images', blank=True),
        ),
    ]
