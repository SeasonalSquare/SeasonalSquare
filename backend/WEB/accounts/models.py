from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Vegi(models.Model):
    vegi_type = models.CharField(max_length=50)


class Allergy(models.Model):
    aller_type = models.TextField()


class User(AbstractUser):
    allergy = models.ManyToManyField(
        Allergy,
        blank=True, null=True,
        related_name = 'Allergy',
    )
    vegi = models.ForeignKey(
        Vegi,
        on_delete=models.CASCADE,
        blank=True, null=True
        )

