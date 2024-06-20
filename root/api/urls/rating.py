from ..views.rating import(
    RatingList
)
from django.urls import path

urlpatterns = [
    path('api/rating/list/', RatingList.as_view(), name = 'api-rating-list')
]
