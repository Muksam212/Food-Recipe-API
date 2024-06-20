from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from root.utils import BaseModel
from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null = True, blank = False)
    tc = models.CharField(max_length=255, null = True, blank = False)  # This is the 'tc' field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return f"{self.is_admin}"