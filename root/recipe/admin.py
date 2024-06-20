from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register([Category, MealPlan, Recipe, ShoppingList, Rating, Review, SharedRecipe])