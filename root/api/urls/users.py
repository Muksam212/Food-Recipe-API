from django.urls import path
from ..views.users import (
    UserRegistrationView, UserLoginView, UserListView, UserProfileView, UserChangePasswordView,
    UserUpdateView
)

urlpatterns = [
    path('user/register/', UserRegistrationView.as_view(), name = 'api-user-register'),
    path('user/login/', UserLoginView.as_view(), name = 'api-user-login'),

    path('user/list/', UserListView.as_view(), name = 'user-list'),
    path('user/profile/', UserProfileView.as_view(), name = 'user-profile'),

    path('user/password/change/', UserChangePasswordView.as_view(), name = 'password-change'),


    path('user/update/<int:id>/', UserUpdateView.as_view(), name = 'user-update')
]
