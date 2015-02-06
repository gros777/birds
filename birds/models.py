from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class SuperiorTaxon(models.Model):
    reino = models.CharField(max_length=200, verbose_name='Kingdom')
    philum = models.CharField(max_length=200, verbose_name='Phylum')
    t_class = models.CharField(max_length=200, verbose_name='Class')
    
    def __str__(self):
        return "Reign: '%s', Philum: '%s', Class = '%s'" % (
        self.reino, self.philum, self.t_class)

class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Order Name')
    superior_taxon = models.ForeignKey(SuperiorTaxon, verbose_name='Higer classification')

    def __str__(self):
        return "%s" % (self.order_name)

class Specimen(models.Model):
    order = models.ForeignKey(Order, verbose_name='Order')
    family = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, verbose_name='Genus')
    species = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    bibliography = models.CharField(max_length=200)

    def scientific_name(self):
        return self.genre + ' ' + self.species
    
    def __str__(self):
        return  ("Specimen(Scientific Name: %s, Common name: %s)" % (
            self.scientific_name(), self.common_name))

class Variety(models.Model):
    description = models.CharField(max_length=200, verbose_name='Description')
    sighting_place = models.CharField(max_length=200, verbose_name='Place of Sight')
    sighting_date = models.DateTimeField('Date of Sight')
    specimen = models.ForeignKey(Specimen)
    
    # bynary field management
    # _image = models.CharField(db_column='image',
    #         blank=True)
    # def set_image(self, image):
    #     self._image = base64.encodestring(data)

    # def get_image(self):
    #     return base64.decodestring(self._image)

    # image = property(get_image, set_image)

    def __str__(self):
        return ("Variety(%s, Sight place: %s)" % (
                self.description, self.sighting_place))

class VarietyImages(models.Model):
    variety = models.ForeignKey(Variety)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
