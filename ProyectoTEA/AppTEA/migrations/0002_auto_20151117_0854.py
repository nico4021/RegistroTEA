# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AppTEA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='periodo',
            field=models.CharField(default=datetime.datetime(2015, 11, 17, 11, 53, 39, 695000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='texto',
            field=models.CharField(default='lorem ipsum', max_length=4000),
            preserve_default=False,
        ),
    ]
