# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('order', models.CharField(max_length=200)),
                ('family', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200, verbose_name='Genus')),
                ('species', models.CharField(max_length=200)),
                ('common_name', models.CharField(max_length=200)),
                ('bibliography', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuperiorTaxon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('reino', models.CharField(max_length=200, verbose_name='Kingdom')),
                ('philum', models.CharField(max_length=200, verbose_name='Phylum')),
                ('t_class', models.CharField(max_length=200, verbose_name='Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('sighting_place', models.CharField(max_length=200, verbose_name='Place of Sight')),
                ('sighting_date', models.DateTimeField(verbose_name='Date of Sight')),
                ('specimen', models.ForeignKey(to='birds.Specimen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VarietyImages',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('variety', models.ForeignKey(to='birds.Variety')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='specimen',
            name='superior_taxon',
            field=models.ForeignKey(to='birds.SuperiorTaxon', verbose_name='Higer classification'),
            preserve_default=True,
        ),
    ]
