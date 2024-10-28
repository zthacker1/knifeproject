# knifeapi/models/blade_type.py

from django.db import models


class BladeType(models.Model):
    FIXED_BLADE = "fixed_blade"
    FOLDER = "folder"
    BALISONG = "balisong"
    OTHER = "other"

    TYPE_CHOICES = [
        (FIXED_BLADE, "Fixed Blade"),
        (FOLDER, "Folder"),
        (BALISONG, "Balisong"),
        (OTHER, "Other"),
    ]

    # Field name should be `type`
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)

    def __str__(self):
        return self.get_type_display()
