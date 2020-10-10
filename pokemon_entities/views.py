import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude, pokemon.longitude,
            pokemon.pokemon.title_ru, request.build_absolute_uri(pokemon.pokemon.img_url.url))

    pokemons_on_page = Pokemon.objects.all()

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = PokemonEntity.objects.filter(pokemon=pokemon_id)
    pokemon = Pokemon.objects.get(pokemon_id=pokemon_id)
    pokemon_on_page = {
        'pokemon_id': pokemon.pokemon_id,
        'img_url': pokemon.img_url.url,
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'previous_evolution': pokemon.previous_evolution,
        'next_evolution': pokemon.next_evolution.all().first(),
    }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons:
        add_pokemon(
            folium_map, pokemon_entity.latitude, pokemon_entity.longitude,
            pokemon_entity.pokemon.title_ru, request.build_absolute_uri(pokemon_entity.pokemon.img_url.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_on_page})
