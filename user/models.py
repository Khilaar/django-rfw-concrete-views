from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = "email"

    #Additional fields required when using createsuperuser
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
