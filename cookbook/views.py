from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cookbook.models import Cookbook
from cookbook.serializers import CookbookSerializer, CreateCookbookSerializer


# Create your views here.

# Create your views here.
class ListCreateCookbookView(GenericAPIView):
    queryset = Cookbook.objects.all()
    #serializer_class = CookbookSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateCookbookSerializer
        return CookbookSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = self.request.user
        serializer.save()
        return Response(serializer.data)


class RetrieveUpdateDeleteCookbookView(GenericAPIView):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)