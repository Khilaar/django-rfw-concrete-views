from django.urls import path

from cookbook.views import ListCreateCookbookView, RetrieveUpdateDeleteCookbookView

urlpatterns = [
    path("", ListCreateCookbookView.as_view()),
    path("<int:pk>/", RetrieveUpdateDeleteCookbookView.as_view()),
    path("own/", ListCreateCookbookView.as_view())
]