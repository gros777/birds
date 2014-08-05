from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # Python 3: def __str__(self):
        return self.choice_text


class SuperiorTaxon(models.Model):
    reino = models.CharField(max_length=200)
    philum = models.CharField(max_length=200)
    t_class = models.CharField(max_length=200)
    
    def __str__(self):
        return "SuperiorTaxon(Reign: '%s', Philum: '%s', Class = '%s')" % (
        self.reino, self.philum, self.t_class)

class Specimen(models.Model):
    superior_taxon = models.ForeignKey(SuperiorTaxon)
    order = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    common_name = models.CharField(max_length=200)
    bibliography = models.CharField(max_length=200)
    
    def __str__(self):
        return  ("Specimen(Scientific Name: %s, Common name: %s)" % (
            self.genre + " " + self.species, self.common_name))

class Variety(models.Model):
    description = models.CharField(max_length=200)
    sighting_place = models.CharField(max_length=200)
    sighting_date = models.DateTimeField('date of sight')
    specimen = models.ForeignKey(Specimen)
    image = models.ImageField(upload_to='images')
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


