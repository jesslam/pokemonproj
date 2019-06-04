from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PokemonType(models.Model):
    pokemontype=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.pokemontype

    class Meta:
        db_table='pokemontype'
        verbose_name_plural='pokemontypes'

class Pokemon(models.Model):
    pokemonname=models.CharField(max_length=100)
    pokemontype=models.ForeignKey(PokemonType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cp=models.IntegerField
    hp=models.IntegerField
    iv=models.IntegerField

    def __str__(self):
        return self.pokemonname

    class Meta:
        db_table='pokemon'
        verbose_name_plural='pokemons'

class FastMove(models.Model):
    fastmove=models.CharField(max_length=100)

    def __str__(self):
        return self.fastmove
    
    class Meta:
        db_table='fastmove'
        verbose_name_plural='fastmoves'

class ChargeMove(models.Model):
    chargemove=models.CharField(max_length=100)

    def __str__(self):
        return self.chargemove

    class Meta:
        db_table='chargemove'
        verbose_name_plural='chargemoves'


