from django.db import models  # noqa F401
from django.utils.timezone import now

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pokemons", null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    append_at = models.DateTimeField(blank=True, null=True)
    disappeared_at = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pokemon} - lat: {self.lat}; lon: {self.lon}"
