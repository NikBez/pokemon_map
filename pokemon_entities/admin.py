from django.contrib import admin
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_en', 'description', 'parent']

@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ['pokemon', 'lat', 'lon', 'append_at', 'disappeared_at', 'level']
