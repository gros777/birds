from django.contrib import admin
from birds.models import *

class VarietyInline(admin.StackedInline):
    model = Variety
    extra = 1

class VarietyImagesInline(admin.TabularInline):
    model = VarietyImages

class SuperiorTaxonAdmin(admin.ModelAdmin):
    fields = ['reino', 'philum', 't_class']
    list_display = ('reino', 'philum', 't_class')

class OrderAdmin(admin.ModelAdmin):
    fields = ['superior_taxon','order_name']
    list_display = ('order_name', 'superior_taxon')
    search_fields = ['order_name']

class SpecimenAdmin(admin.ModelAdmin):
    fields = ['order', 'family',
              'genre', 'species', 
              'common_name', 'bibliography']
    list_display = ('order',
                    'common_name', 
                    'scientific_name', 
                    'family', 
                    'genre', 
                    'species')
    list_filter = ['family', 'genre']
    search_fields = ['order',
                     'common_name', 
                     'family', 
                     'species']

class VarietyAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,               {'fields' : ['specimen', 'description']}),
        ('Sight Information', {'fields' : ['sighting_place', 'sighting_date']})
    ]
    list_display = ('description', 
                    'sighting_place',
                    'sighting_date')
    list_filter = ['sighting_date', 
                   'sighting_place']
    search_fields = ['description', 
                    'sighting_place',]

    inlines = [VarietyImagesInline]

# Register your models here
admin.site.register(SuperiorTaxon, SuperiorTaxonAdmin)
admin.site.register(Specimen, SpecimenAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Order, OrderAdmin)