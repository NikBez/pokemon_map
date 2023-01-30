from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField("Название (русский)", max_length=200, default="")
    title_en = models.CharField("Название (Английский)", max_length=200, blank=True, default="")
    title_jp = models.CharField("Назвагие (Японский)", max_length=200, blank=True, default="")
    description = models.TextField("Описание", default="", blank=True)
    image = models.ImageField( "Изображение", upload_to="pokemons", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="childs", verbose_name="Предок")


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="entities", verbose_name="Покемон")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appear_at = models.DateTimeField( "Время появления")
    disappeared_at = models.DateTimeField("Время исчезновения")
    level = models.IntegerField("Уровень", null=True, blank=True)
    health = models.IntegerField("Здоровье", null=True, blank=True)
    strength = models.IntegerField("Сила", null=True, blank=True)
    defense = models.IntegerField("Защита", null=True, blank=True)
    stamina = models.IntegerField("Выносливость", null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon} - lat: {self.lat}; lon: {self.lon}"
