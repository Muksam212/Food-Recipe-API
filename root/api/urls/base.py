from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .category import urlpatterns as category_urlpatterns
from .users import urlpatterns as users_urlpatterns
from .recipe import urlpatterns as recipe_urlpatterns
from .mealplan import urlpatterns as meal_plan_urlpatterns
from .rating import urlpatterns as rating_urlpatterns
from .review import urlpatterns as review_urlpatterns
from .sharedrecipe import urlpatterns as shared_urlpatterns
from .shoppinglist import urlpatterns as shopping_list_urlpatterns



#Implementing swaggers

schema_view = get_schema_view(
    openapi.Info(
        title="Food Recipe API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = (
    [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
             name = 'schema-swagger-ui'),
        path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name = 'schema-redoc'),
    ]
    +users_urlpatterns
    +category_urlpatterns
    +recipe_urlpatterns
    +rating_urlpatterns
    +shared_urlpatterns
    +review_urlpatterns
    +shopping_list_urlpatterns
    +meal_plan_urlpatterns
)
