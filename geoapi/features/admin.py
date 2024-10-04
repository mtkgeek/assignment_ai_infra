from django.contrib import admin
from .models import GeoFeature


@admin.register(GeoFeature)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
