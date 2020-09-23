from django.db import models
import json

# Create your models here.

class Grocery(models.Model):
    name = models.CharField(max_length=50)
    calorie = models.IntegerField()


class Recipe(models.Model):
    img = models.CharField(max_length=150)
    ingredients = models.ManyToManyField(
        Grocery,
        blank=True, null=True,
        related_name = 'recipe',
    )
    content = models.TextField()

    def set_content(self, json_file):
        self.content = json.dump(json_file)

    def get_content(self):
        return json.loads(self.content)



