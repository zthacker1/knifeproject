from django.db import models


class Knife(models.Model):
    userId = models.ForeignKey("User", on_delete=models.CASCADE, related_name="knives")
    name = models.CharField(max_length=155)
    price = models.IntegerField()
    typeId = models.ForeignKey("knifeapi.Type", on_delete=models.CASCADE)
    description = models.CharField(max_length=155)

    # Avoid reverse accessor conflicts
    mods = models.ManyToManyField("Mod", related_name="knives_with_mods")

    def __str__(self):
        return self.name
