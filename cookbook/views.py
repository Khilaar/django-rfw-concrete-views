from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from cookbook.models import Cookbook
from cookbook.permissions import IsOwnerOrReadOnly
from cookbook.serializers import CookbookSerializer, CreateCookbookSerializer


# Create your views here.

# Create your views here.
class ListCreateCookbookView(ListCreateAPIView):
    """
    get: Returns a list of all cookbooks
    post: Creates a new Cookbook
    """
    #queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        recipes = self.request.query_params.get('recipes')

        if recipes:
            return Cookbook.objects.filter(recipes__title__icontains=recipes)

        if search:
            return Cookbook.objects.filter(title__icontains=search)
        return Cookbook.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListLoggedInUserCookbooks(ListAPIView):
    serializer_class = CookbookSerializer
    def get_queryset(self):
        return Cookbook.objects.filter(owner=self.request.user)



class RetrieveUpdateDeleteCookbookView(RetrieveUpdateDestroyAPIView):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    permission_classes = [IsOwnerOrReadOnly]

