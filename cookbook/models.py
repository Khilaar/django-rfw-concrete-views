from django.contrib.auth import get_user_model
from django.db import models

from recipe.models import Recipe

User = get_user_model()

# Create your models here.
class Cookbook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    recipes = models.ManyToManyField(to=Recipe)
    owner = models.ForeignKey(to=User, on_delete=models.PROTECT)