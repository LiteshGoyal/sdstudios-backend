from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . import serializers
from . import models


class UserCreateView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()