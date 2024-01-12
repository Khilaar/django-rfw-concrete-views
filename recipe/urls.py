from django.urls import path

from recipe.views import ListCreateRecipeView, RetrieveUpdateDeleteRecipeView

urlpatterns = [
    path("", ListCreateRecipeView.as_view()),
    path("<int:pk>/", RetrieveUpdateDeleteRecipeView.as_view())
]