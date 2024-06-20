from rest_framework import serializers
from users.models import User

from ..serializers.recipe import RecipeSerializer
from ..serializers.review import ReviewSerializer
from ..serializers.sharedrecipe import SharedRecipeSerializer
from ..serializers.mealplan import MealPlanSerializer
from ..serializers.shoppinglist import ShoppingSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('id','email', 'name', 'tc', 'password', 'password2')
        extra_kwargs={
        'password':{'write_only':True}
        }

    #validate password and confirm password while registration
    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ("email", "password")


class UserListSerializer(serializers.ModelSerializer):
    #nested serializer
    users_recipe = RecipeSerializer(many = True)
    users_reviews = ReviewSerializer(many = True)
    shared_by = SharedRecipeSerializer(many = True)
    shared_with = SharedRecipeSerializer(many = True)
    users_meal_plan = MealPlanSerializer(many = True)
    users_shopping_list = ShoppingSerializer(many = True)
    class Meta:
        model = User
        fields = ("id", "email", "name", "tc", "is_active", "is_admin","users_recipe", "users_reviews", "shared_by",
                  "shared_with", "users_meal_plan", "users_shopping_list")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name")



class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={"input_type":"password"}, write_only = True)
    password2 = serializers.CharField(max_length=255, style={"input_type":"password"}, write_only = True)

    class Meta:
        model = User
        fields = ("password", "password2")

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        print(user,"user")
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs