from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class SuperiorTaxon(models.Model):
    reino = models.CharField(max_length=200, verbose_name='Kingdom')
    phylum = models.CharField(max_length=200, verbose_name='Phylum')
    t_class = models.CharField(max_length=200, verbose_name='Class')

    def __str__(self):
        return "Reign: '%s', Phylum: '%s', Class = '%s'" % (
            self.reino, self.phylum, self.t_class)


class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Order')
    superior_taxon = models.ForeignKey(SuperiorTaxon, verbose_name='Higer classification')

    def __str__(self):
        return "%s" % self.order_name


class Family(models.Model):
    name = models.CharField(max_length=200, verbose_name='Family')
    order = models.ForeignKey(Order)

    def __str__(self):
        return "%s" % self.name


class Genus(models.Model):
    name = models.CharField(max_length=200, verbose_name='Genus')
    family = models.ForeignKey(Family, unique=False)

    def __str__(self):
        return "%s" % self.name


class Specimen(models.Model):
    genus = models.ForeignKey(Genus)
    name = models.CharField(max_length=200, verbose_name='Specimen')
    common_name = models.CharField(max_length=200)
    bibliography = models.CharField(max_length=200)

    def scientific_name(self):
        return self.genus.name + ' ' + self.name

    def __str__(self):
        return ("Specimen(Scientific Name: %s, Common name: %s)" % (
            self.scientific_name(), self.common_name))


class Variety(models.Model):
    name = models.CharField(max_length=200, verbose_name='Var')
    specimen = models.ForeignKey(Specimen)

    def __str__(self):
        return ("%s, Var %s" % (
            self.specimen.name, self.name))


# Implement some validation to verified that at least one of the foreign key be added
class BirdImage(models.Model):
    variety = models.ForeignKey(Variety, null=True, blank=True)
    specimen = models.ForeignKey(Specimen, null=True, blank=True)
    author = models.CharField(max_length=200)
    sighting_place = models.CharField(max_length=200, verbose_name='Place of Sight', null=True)
    sighting_date = models.DateTimeField('Date of Sight', null=True)
    image = models.ImageField(upload_to='images')
