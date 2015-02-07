# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('sighting_place', models.CharField(verbose_name='Place of Sight', max_length=200)),
                ('sighting_date', models.DateTimeField(verbose_name='Date of Sight')),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Family', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Genus', max_length=200)),
                ('family', models.ForeignKey(to='birds.Family')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('order_name', models.CharField(verbose_name='Order', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Specimen', max_length=200)),
                ('common_name', models.CharField(max_length=200)),
                ('bibliography', models.CharField(max_length=200)),
                ('genus', models.ForeignKey(to='birds.Genus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuperiorTaxon',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('reino', models.CharField(verbose_name='Kingdom', max_length=200)),
                ('phylum', models.CharField(verbose_name='Phylum', max_length=200)),
                ('t_class', models.CharField(verbose_name='Class', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Var', max_length=200)),
                ('specimen', models.ForeignKey(to='birds.Specimen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='superior_taxon',
            field=models.ForeignKey(verbose_name='Higer classification', to='birds.SuperiorTaxon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='family',
            name='order',
            field=models.ForeignKey(to='birds.Order'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='birdimage',
            name='specimen',
            field=models.ForeignKey(blank=True, to='birds.Specimen', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='birdimage',
            name='variety',
            field=models.ForeignKey(blank=True, to='birds.Variety', null=True),
            preserve_default=True,
        ),
    ]
