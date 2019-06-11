from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PokemonType(models.Model):
    pokemontype=models.CharField(max_length=100)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pokemontype

    class Meta:
        db_table='pokemontype'
        verbose_name_plural='pokemontypes'

class Pokemon(models.Model):
    pokemonname=models.CharField(max_length=100)
    pokemonbase=models.CharField(max_length=100)
    pokemontype=models.ForeignKey(PokemonType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cp=models.IntegerField(null=True, blank=True)
    hp=models.IntegerField(null=True, blank=True)
    level=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.pokemonname

    class Meta:
        db_table='pokemon'
        verbose_name_plural='pokemons'


class Evaluation(models.Model):
    pokemonname=models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING, null=True, blank=True)
    attacknum=models.IntegerField(null=True, blank=True)
    defensenum=models.IntegerField(null=True, blank=True)
    staminanum=models.IntegerField(null=True, blank=True)
    IVpercent=models.IntegerField(null=True, blank=True)
    IVname=models.CharField(max_length=20)

    def __str__(self):
        return self.IVname + " " + str(self.IVpercent) + "%"
    
    class Meta:
        db_table='evaluation'
        verbose_name_plural='evaluations'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    pokemonname=models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

