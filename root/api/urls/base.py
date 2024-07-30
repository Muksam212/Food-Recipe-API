from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


from .category import urlpatterns as category_urlpatterns
from .users import urlpatterns as users_urlpatterns
from .recipe import urlpatterns as recipe_urlpatterns
from .mealplan import urlpatterns as meal_plan_urlpatterns
from .rating import urlpatterns as rating_urlpatterns
from .review import urlpatterns as review_urlpatterns
from .sharedrecipe import urlpatterns as shared_urlpatterns
from .shoppinglist import urlpatterns as shopping_list_urlpatterns


from django.urls import path, include


urlpatterns = [
    path('', include(category_urlpatterns)),
    path('', include(users_urlpatterns)),
    path('', include(recipe_urlpatterns)),
    path('', include(meal_plan_urlpatterns)),
    path('', include(rating_urlpatterns)),
    path('', include(review_urlpatterns)),
    path('', include(shared_urlpatterns)),
    path('', include(shopping_list_urlpatterns))

]


# #Implementing swaggers
# urlpatterns = (
#     [
#         path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
#              name = 'schema-swagger-ui'),
#         path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name = 'schema-redoc'),
#     ]
#     +users_urlpatterns
#     +category_urlpatterns
#     +recipe_urlpatterns
#     +rating_urlpatterns
#     +shared_urlpatterns
#     +review_urlpatterns
#     +shopping_list_urlpatterns
# )
