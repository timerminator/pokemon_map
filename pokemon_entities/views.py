import folium

from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, level, strongth, health, defence, stamina, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    popup_text = """    {}
                    <br>level: {}  
                    <br>strongth: {}
                    <br>health: {}
                    <br>defence: {}
                    <br>stamina: {}
    """.format(name, level, strongth, health, defence, stamina)
    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_text, max_width=200),
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude, pokemon.longitude,
            pokemon.pokemon.title_en, pokemon.level, pokemon.strongth, pokemon.health, pokemon.defence, pokemon.stamina,
            request.build_absolute_uri(pokemon.pokemon.img_url.url))

    pokemon_types = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemon_types:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.img_url.url,
            'title_ru': pokemon.title_ru,

        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = PokemonEntity.objects.filter(pokemon=int(pokemon_id))
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    pokemon_on_page = {
        'pokemon_id': pokemon.id,
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
            pokemon_entity.pokemon.title_en, pokemon_entity.level, pokemon_entity.strongth,
            pokemon_entity.health, pokemon_entity.defence, pokemon_entity.stamina,
            request.build_absolute_uri(pokemon_entity.pokemon.img_url.url))

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_on_page})
