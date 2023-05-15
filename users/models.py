from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,  error_messages={"unique": ("This field must be unique.")})
    username = models.CharField(unique=True, max_length=130,  error_messages={"unique": ("A user with that username already exists.")})