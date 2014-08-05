from django.contrib import admin
from birds.models import *
# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(SuperiorTaxon)
admin.site.register(Specimen)
admin.site.register(Variety)