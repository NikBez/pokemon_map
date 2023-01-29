from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pokemon_imgs", null=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"lat: {self.lat}; lon: {self.lon}"
