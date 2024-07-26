from django.core.exceptions import ValidationError
from django.db import models


def OnlyLettersValidator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")