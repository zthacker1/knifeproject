from django.db import models
from django.conf import settings
from .blade_type import BladeType
from .mod import Mod


class Knife(models.Model):
    userId = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="knives"
    )
    name = models.CharField(max_length=155)
    price = models.IntegerField()
    bladeTypeId = models.ForeignKey(BladeType, on_delete=models.CASCADE)
    description = models.CharField(max_length=155)

    # Many-to-Many relationship with Mod, avoiding reverse accessor conflicts
    mods = models.ManyToManyField(Mod, related_name="knives_with_mods")

    def __str__(self):
        return self.name
