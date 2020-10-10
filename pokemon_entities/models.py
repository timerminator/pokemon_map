from django.db import models


class Pokemon(models.Model):
    pokemon_id = models.AutoField(primary_key=True)
    title_ru = models.CharField(verbose_name='Название', max_length=200)
    title_en = models.CharField(verbose_name='Название на английском', max_length=200, blank=True, default=None)
    title_jp = models.CharField(verbose_name='Название на японском', max_length=200, blank=True, default=None)
    img_url = models.ImageField(verbose_name='Изображение', upload_to='pokemons', blank=True, default=None)
    description = models.TextField(verbose_name='Описание', blank=True, default=None)
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default = None,
                                           related_name='next_evolution', verbose_name='Предыдущая эволюция',)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1, verbose_name='Тип покемона')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появляется', blank=True, null=True, default=None)
    disappeared_at = models.DateTimeField(verbose_name='Изчезает', blank=True, null=True, default=None)
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True, default=None)
    health = models.IntegerField(verbose_name='Здоровье', blank=True, null=True, default=None)
    strongth = models.IntegerField(verbose_name='Сила', blank=True, null=True, default=None)
    defence = models.IntegerField(verbose_name='Защита', blank=True, null=True, default=None)
    stamina = models.IntegerField(verbose_name='Выносливость', blank=True, null=True, default=None)

    def __str__(self):
        return '{} {} уровня'.format(self.pokemon.title_ru, self.level)
