from django.db import models


class Type(models.Model):
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

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=OTHER)

    def __str__(self):
        return (
            self.get_type_display()
        )  # Returns the human-readable name of the selected choice
