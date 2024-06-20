from django.urls import path
from ..views.review import (
    ReviewList,
    ReviewDetails
)

urlpatterns = [
    path('api/review/list/', ReviewList.as_view(), name = 'review-list'),
    path('api/review/update/<int:id>/', ReviewDetails.as_view(), name = 'review-details')
]
