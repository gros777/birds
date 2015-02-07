# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdimage',
            name='sighting_date',
            field=models.DateTimeField(null=True, verbose_name='Date of Sight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='birdimage',
            name='sighting_place',
            field=models.CharField(max_length=200, null=True, verbose_name='Place of Sight'),
            preserve_default=True,
        ),
    ]
