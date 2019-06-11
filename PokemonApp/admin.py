from django.contrib import admin
from .models import PokemonType, Pokemon, Evaluation, Review

# Register your models here.
admin.site.register(PokemonType)
admin.site.register(Pokemon)
admin.site.register(Evaluation)
admin.site.register(Review)