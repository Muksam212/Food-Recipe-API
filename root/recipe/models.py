from django.db import models

from root.utils import BaseModel
from users.models import User
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique = True, blank = True, null = False)

    def __str__(self):
        return f'{self.name}'
    
class Recipe(BaseModel):
    title = models.CharField(max_length=200, unique = True)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "users_recipe")
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class MealPlan(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "users_meal_plan")
    date = models.DateField()
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return f"{self.user.name}'s meal plan for {self.date}"
    

class ShoppingList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "users_shopping_list")
    recipes = models.ManyToManyField(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}'s shopping list"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "users_rating")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s rating for {self.recipe.title}"
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "users_reviews")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()

    def __str__(self):
        return f"{self.user.name}'s review for {self.recipe.title}"
    
class SharedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="users_shared_recipe")
    shared_by = models.ForeignKey(User, related_name='shared_by', on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, related_name='shared_with', on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.shared_by.name} shared {self.recipe.title} with {self.shared_with.name}"