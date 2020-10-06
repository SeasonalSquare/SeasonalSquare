from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Recipe
from accounts.serializers import AllergySerializer



class RecipeListSerializer(serializers.ModelSerializer):
    allergies = AllergySerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'image', 'main_grocery', 'title', 'writer', 'allergies')


class RecipeSerializer(serializers.ModelSerializer):
    allergies = AllergySerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
