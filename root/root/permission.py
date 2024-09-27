from django.db.models import Q
from django.shortcuts import redirect

from rest_framework.exceptions import PermissionDenied



class IsCookMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "Cook":
            return super().dispatch(request, *args, **kwargs)
        
        raise PermissionDenied
        
class IsAdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Admin":
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
    


class IsPlannerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Planner":
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
    
class IsEnthusiastMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "Enthusiast":
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied