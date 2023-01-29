from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField("Название (русский)", max_length=200)
    title_en = models.CharField("Название (Английский)", max_length=200, blank=True, null=True)
    title_jp = models.CharField("Назвагие (Японский)", max_length=200, blank=True, null=True )
    description = models.TextField("Описание", null=True, blank=True)
    image = models.ImageField( "Изображение", upload_to="pokemons", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="child", verbose_name="Предок")


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="enteties", verbose_name="Покемон")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    append_at = models.DateTimeField( "Время появления")
    disappeared_at = models.DateTimeField("Время исчезновения")
    level = models.IntegerField("Уровень", default=0)
    health = models.IntegerField("Здоровье", default=0)
    strength = models.IntegerField("Сила", default=0)
    defense = models.IntegerField("Защита", default=0)
    stamina = models.IntegerField("Выносливость", default=0)

    def __str__(self):
        return f"{self.pokemon} - lat: {self.lat}; lon: {self.lon}"
