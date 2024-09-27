from rest_framework import serializers
from users.models import User

from ..serializers.recipe import RecipeSerializer
from ..serializers.review import ReviewSerializer
from ..serializers.sharedrecipe import SharedRecipeSerializer
from ..serializers.mealplan import MealPlanSerializer
from ..serializers.shoppinglist import ShoppingSerializer
from ..serializers.rating import RatingSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)
    role = serializers.CharField(write_only = True, max_length = 20)
    bio = serializers.CharField(write_only = True, max_length = 20)
    class Meta:
        model = User
        fields = ('username', 'email', 'password',  'confirm_password', 'role', 'bio')
        extra_kwargs={
        'password':{'write_only':True},
        'confirm_password':{'write_only':True}
        }

    #validate password and confirm password while registration
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    
    # Override the create method to handle password hashing
    def create(self, validated_data):
        # Remove the password2 field from validated data as it's not needed for creation
        validated_data.pop('confirm_password')

        # Create a new user instance
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            profile_image=validated_data.get('profile_image', None),
            role=validated_data['role'],
        )
        
        # Set the password (hashing it)
        user.set_password(validated_data['password'])
        
        # Save the user to the database
        user.save()

        return user

    
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]


class UserListSerializer(serializers.ModelSerializer):
    #nested serializer
    # users_recipe = RecipeSerializer(many = True)
    # users_reviews = ReviewSerializer(many = True)
    # shared_by = SharedRecipeSerializer(many = True)
    # shared_with = SharedRecipeSerializer(many = True)
    # users_meal_plan = MealPlanSerializer(many = True)
    # users_shopping_list = ShoppingSerializer(many = True)
    users_rating = RatingSerializer(many = True)
    class Meta:
        model = User
        fields = ("id", "email", "username","role", "users_rating")


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = User
        fields = ("id","email", "username", "role")



class UserChangePasswordSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["old_password", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"error": "The Password confirmation does not match"}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
    