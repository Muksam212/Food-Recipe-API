from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from root.utils import BaseModel
from .managers import CustomUserManager
# Create your models here.

USER_TYPE = (
    ("Admin", "Admin"),
    ("Cook", "Cook"),
    ("Planner", "Planner"),
    ("Enthusiast", "Enthusiast"),
    ("None", "None")
)

class User(BaseModel,AbstractUser):
    username = models.CharField(max_length=100, unique = True, null = True, blank = False)
    email = models.EmailField(unique=True, null = True, blank = False)
    bio = models.TextField(null = True, blank = True)
    profile_image = models.ImageField(upload_to='profile_images/', null = True, blank = False)
    role = models.CharField(max_length=20, choices = USER_TYPE, default = "NOne")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"