from django.core.validators import MinLengthValidator
from django.db import models
from Frutipedia.fruits.validators import OnlyLettersValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2),
                    OnlyLettersValidator],
    )

    Image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField()

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='fruits'
    )

