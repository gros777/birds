# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0003_auto_20150203_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimen',
            name='bird_order',
        ),
        migrations.AlterField(
            model_name='specimen',
            name='order',
            field=models.ForeignKey(null=True, verbose_name='Order', to='birds.Order'),
            preserve_default=True,
        ),
    ]
