from django.core.validators import MinLengthValidator
from django.db import models
from django_plant.web.validators import profile_name_validator, plant_name_validator


# Create your models here.
class Profile(models.Model):

    username = models.CharField(
        null = False,
        blank = False,
        max_length=10,
        validators=[
            MinLengthValidator(2),
        ]
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        verbose_name="First Name",
        max_length=20,
        validators=[
            profile_name_validator
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        verbose_name="Last Name",
        max_length=20,
        validators=[
            profile_name_validator
        ]
    )

    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        null=True,
        blank=True
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username}--<<{self.first_name} {self.last_name}>>--'


class Plant(models.Model):
    TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    type = models.CharField(
        null=False,
        blank=False,
        verbose_name="Type",
        max_length=14,
        choices=TYPES,
        default="Indoor Plants",
    )

    name = models.CharField(
        null=False,
        blank=False,
        verbose_name="Name",
        validators=[
            MinLengthValidator(2),
            plant_name_validator
        ],
        max_length=20
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="Description"
    )

    price = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Price"
    )

    def __str__(self):
        return f'{self.name} -- {self.type}'