# Generated by Django 2.2.3 on 2020-11-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20201114_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='strong_against',
            field=models.ManyToManyField(related_name='_pokemonelementtype_strong_against_+', to='pokemon_entities.PokemonElementType'),
        ),
    ]