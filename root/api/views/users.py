from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from ..views.renderers import UserRenderer

from ..serializers.users import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
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


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            user_data = self.serializer_class(user).data

            return Response({
                "User":user_data, "msg":"Registration Successful"
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

class UserListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filterset_class = UserSetFilter

class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "username or password is not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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


class UserChangePasswordView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset = None):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # Return a custom response with message
        return Response({
            'message': 'Password has been reset successfully.'
        }, status=status.HTTP_200_OK)
    

class UserDeleteView(DestroyAPIView):
    serializer_class = UserProfileSerializer
    model = User
    lookup_field = "id"