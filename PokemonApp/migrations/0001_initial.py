# Generated by Django 2.2 on 2019-06-04 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chargemovename', models.CharField(max_length=50)),
                ('chargemovetype', models.CharField(max_length=50)),
                ('chargemovetype2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'chargemoves',
                'db_table': 'chargemove',
            },
        ),
        migrations.CreateModel(
            name='FastMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fastmovename', models.CharField(max_length=50)),
                ('fastmovetype', models.CharField(max_length=50)),
                ('fastmovetype2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'fastmoves',
                'db_table': 'fastmove',
            },
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemontype', models.CharField(max_length=100)),
                ('pokemontype2', models.CharField(max_length=100)),
                ('typedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'pokemontypes',
                'db_table': 'pokemontype',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemonname', models.CharField(max_length=100)),
                ('pokemonbase', models.CharField(max_length=100)),
                ('pokemontype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PokemonApp.PokemonType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pokemons',
                'db_table': 'pokemon',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IVname', models.CharField(max_length=20)),
                ('chargemovenum', models.ManyToManyField(to='PokemonApp.ChargeMove')),
                ('fastmovenum', models.ManyToManyField(to='PokemonApp.FastMove')),
            ],
            options={
                'verbose_name_plural': 'evaluations',
                'db_table': 'evaluation',
            },
        ),
    ]