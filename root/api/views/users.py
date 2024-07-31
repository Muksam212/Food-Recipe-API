from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from ..views.renderers import UserRenderer

from ..serializers.users import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from .filters import *

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = UserRegistrationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"msg":"Registration Successful"}, status = status.HTTP_201_CREATED)
    

class UserListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filterset_class = UserSetFilter

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    


class UserUpdateView(APIView):
    def patch(self, request, id = None):
        user_update = get_object_or_404(User, id = id)
        serializer = UserRegistrationSerializer(user_update, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Updated Successful"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format = None):
        serializers = UserChangePasswordSerializer(data = request.data, context = {"user":request.user})
        serializers.is_valid(raise_exception = True)
        return Response({"msg":"Password Change Successful"}, status = status.HTTP_200_OK)
    

# from rest_framework.views import APIView

# class UserDelete(APIView):
#     def post(self, request, pk = None):
#         user = get_object_or_404(User, pk = pk)
#         user.delete()
#         return Response({"msg":"deleted"}, status = status.HTTP_404_NOT_FOUND)