from rest_framework import serializers
from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        existing_recipe = Recipe.objects.filter(title__exact=value).exclude(pk=self.instance.pk).first()
        if existing_recipe:
            raise serializers.ValidationError("This recipe already exists.")
        return value

    class Meta:
        model = Recipe
        fields = '__all__'
