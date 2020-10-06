from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Recipe
from .serializers import RecipeSerializer, RecipeListSerializer


# Create your views here.
@api_view(['GET'])
def grocery(request, grocery_name):
    recipes = Recipe.objects.filter(main_grocery=grocery_name)
    serializer = RecipeListSerializer(recipes, many=True)
    for recipe in serializer.data:
        recipe['pk'] = recipe['id']
    
    return Response(serializer.data)


@api_view(['GET'])
def recipe(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    return Response(recipe.get_content())
