from django.db import models


class KnifeMod(models.Model):
    knifeId = models.ForeignKey(
        "Knife", on_delete=models.CASCADE, related_name="knife_mod_associations"
    )
    modId = models.ForeignKey(
        "Mod", on_delete=models.CASCADE, related_name="mod_associations"
    )

    class Meta:
        unique_together = ("knifeId", "modId")
