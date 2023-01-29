from django.db import models  # noqa F401
from django.utils.timezone import now

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pokemon_imgs", null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    append_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defense = models.IntegerField()
    stamina = models.IntegerField()

    def __str__(self):
        return f"{self.pokemon} - lat: {self.lat}; lon: {self.lon}"
