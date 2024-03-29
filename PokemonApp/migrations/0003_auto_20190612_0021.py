# Generated by Django 2.2 on 2019-06-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokemonApp', '0002_auto_20190611_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='IVpercent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='chargemovenum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='fastmovenum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='staminanum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='cp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemontype',
            name='typedescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
