import folium
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .models import Pokemon, PokemonEntity
from pytz import timezone


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):

    moscow_date_time = localtime(timezone=timezone("Europe/Moscow"))

    db_pokemon_entity = PokemonEntity.objects.filter(appear_at__lt=moscow_date_time,\
                        disappeared_at__gt=moscow_date_time)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in db_pokemon_entity:
        add_pokemon(
            folium_map, entity.lat,
            entity.lon,
            request.build_absolute_uri(entity.pokemon.image.url)
        )
    pokemons_on_page = []
    db_pokemons = Pokemon.objects.all()
    for db_pokemon in db_pokemons:
        image = db_pokemon.image.url if db_pokemon.image else ""
        pokemons_on_page.append({
            'pokemon_id': db_pokemon.id,
            'img_url': image,
            'title_ru': db_pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon.entities.all():
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    parent_img = request.build_absolute_uri(pokemon.parent.image.url) if pokemon.parent else None
    child_img = request.build_absolute_uri(pokemon.childs.first().image.url) if pokemon.childs.first() else None

    pokemon_context = {
        "title_ru":pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,
        "image": pokemon.image.url,
        "previous_evolution": pokemon.parent,
        "previous_evolution_img": parent_img,
        "next_evolution": pokemon.childs.first(),
        "next_evolution_img": child_img,
    }


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_context,
    })
