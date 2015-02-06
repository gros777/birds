# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0004_auto_20150203_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='order',
            field=models.ForeignKey(verbose_name='Order', to='birds.Order'),
            preserve_default=True,
        ),
    ]
