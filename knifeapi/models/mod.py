from django.db import models


class Mod(models.Model):
    BLADE = "blade"
    HANDLE = "handle"
    HARDWARE = "hardware"
    ACCESSORIES = "accessories"
    OTHER = "other"

    MOD_CHOICES = [
        (BLADE, "Blade"),
        (HANDLE, "Handle"),
        (HARDWARE, "Hardware"),
        (ACCESSORIES, "Accessories"),
        (OTHER, "Other"),
    ]

    mod_type = models.CharField(max_length=20, choices=MOD_CHOICES)

    def __str__(self):
        return self.get_mod_type_display()
