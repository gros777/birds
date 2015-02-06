# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirdOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('order_name', models.CharField(verbose_name='Order Name', max_length=200)),
                ('superior_taxon', models.ForeignKey(verbose_name='Higer classification', to='birds.SuperiorTaxon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='specimen',
            name='superior_taxon',
        ),
        migrations.AddField(
            model_name='specimen',
            name='bird_order',
            field=models.ForeignKey(null=True, to='birds.BirdOrder', verbose_name='Order'),
            preserve_default=True,
        ),
    ]
