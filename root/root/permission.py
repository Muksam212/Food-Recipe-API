from django.db.models import Q
from django.shortcuts import redirect

class IsCookMixin(object):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.user_type == "Cook"
    

class IsPlannerMixin(object):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.user_type == "Planner"
    

class IsEnthusiastMixin(object):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == "Enthusiast"
    

class IsAdminMixin(object):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == "Admin"