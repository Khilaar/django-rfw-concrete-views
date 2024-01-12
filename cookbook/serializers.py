from django.contrib.auth.models import User
from rest_framework import serializers

from cookbook.models import Cookbook
from recipe.serializers import RecipeSerializer


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CookbookSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)
    owner = OwnerSerializer()

    class Meta:
        model = Cookbook
        fields = ["id", "title", "description", "created", "updated", "owner", "recipes"]


class CreateCookbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookbook
        fields = ["title", "description"]
        read_only_fields = ["buyer"]
