# Generated by Django 3.1.1 on 2020-10-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_pokemonelementtype_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonelementtype',
            name='img_url',
            field=models.ImageField(blank=True, null=True, upload_to='elements', verbose_name='Изображение'),
        ),
    ]