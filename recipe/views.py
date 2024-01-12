from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


# Create your views here.
class ListCreateRecipeView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RetrieveUpdateDeleteRecipeView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
