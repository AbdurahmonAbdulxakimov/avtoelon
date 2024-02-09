from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import RegexValidator

from common.models import Region, District


class GenderChoise(models.Choices):
    MALE = "Erkak"
    FEMALE = "Ayol"


class User(AbstractUser):
    _phone_validation = RegexValidator(
        regex=r"^?1?\d{9,15}$",
        message="Phone number must be entered in the format: '998901015577'. Up to 12 digits allowed.",
    )

    phone_number = models.CharField(
        validators=[_phone_validation], max_length=12, primary_key=True
    )

    name = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GenderChoise.choices, default=GenderChoise.MALE
    )
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
