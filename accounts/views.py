from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from accounts.models import UserModel

from accounts.models import UserModel
from accounts.serializer import UserModelSerializer




class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        serializer.save()
