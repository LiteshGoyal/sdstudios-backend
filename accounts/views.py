from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserCreateView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class UserLogInView(APIView):
    def post(self,request):
        serializer = serializers.UserLoginSerializer(data= request.data)
        if serializer.is_valid():
            error = None
            try:
                profile = models.Profile.objects.get(email = serializer.validated_data['email'])
                user = profile.user
                if user.check_password(serializer.validated_data['password']):
                    token,created = Token.objects.get_or_create(user=profile.user)
                    _token = token.key
                else:
                    _token = None
                    error = 'Invalid Password!!'
            except models.Profile.DoesNotExist:
                _token = None
                error = 'Invalid Email'
            return Response({'token':_token,'error':error})