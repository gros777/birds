from django.contrib import admin
from birds.models import *


class BirdInline(admin.StackedInline):
    model = Variety
    extra = 1


class BirdImageInline(admin.TabularInline):
    model = BirdImage
    fields = ['author',
              'sighting_place',
              'sighting_date',
              'image']


class SuperiorTaxonAdmin(admin.ModelAdmin):
    fields = ['reino', 'phylum', 't_class']
    list_display = ('reino', 'phylum', 't_class')


class OrderAdmin(admin.ModelAdmin):
    fields = ['superior_taxon', 'order_name']
    list_display = ('order_name', 'superior_taxon')
    search_fields = ['order_name']


class FamilyAdmin(admin.ModelAdmin):
    fields = ['order', 'name']
    list_display = ('order', 'name')
    search_fields = ['name']


class GenusAdmin(admin.ModelAdmin):
    fields = ['family', 'name']
    list_display = ('family', 'name')
    search_fields = ['name']


class SpecimenAdmin(admin.ModelAdmin):
    fields = ['genus',
              'name',
              'common_name',
              'bibliography']
    list_display = ('common_name',
                    'scientific_name',)
    list_filter = ['name', 'genus']
    search_fields = ['common_name',
                     'genus.family',
                     'name']
    inlines = [BirdImageInline]


class VarietyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['specimen', 'name']}),
    ]
    list_display = ('specimen',
                    'name',)
    search_fields = ['name', ]

    inlines = [BirdImageInline]

# Register your models here
admin.site.register(SuperiorTaxon, SuperiorTaxonAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Genus, GenusAdmin)
admin.site.register(Specimen, SpecimenAdmin)
admin.site.register(Variety, VarietyAdmin)
