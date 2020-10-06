from django.db import models
from accounts.models import Allergy
import json

# Create your models here.

class Grocery(models.Model):
    name = models.CharField(max_length=50)
    calorie = models.IntegerField()


class Recipe(models.Model):
    image = models.CharField(max_length=150)
    main_grocery = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        Grocery,
        blank=True,
        related_name = 'ingredients_recipe',
    )
    content = models.TextField()
    allergies = models.ManyToManyField(
        Allergy,
        blank=True,
        related_name = 'allergy_recipe'
    )


    def set_content(self, json_file):
        self.content = json.dumps(json_file)

    def get_content(self):
        return json.loads(self.content)