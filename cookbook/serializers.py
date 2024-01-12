from django.contrib.auth import get_user_model
from rest_framework import serializers

from cookbook.models import Cookbook
from recipe.serializers import RecipeSerializer

User = get_user_model()


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CookbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookbook
        fields = ["id", "title", "description", "created", "updated", "owner", "recipes"]
        read_only_fields = ["owner"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["owner"] = OwnerSerializer(instance.owner).data
        representation["recipes"] = RecipeSerializer(instance.recipes, many=True).data
        return representation


class CreateCookbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookbook
        fields = ["title", "description"]
        read_only_fields = ["buyer"]
