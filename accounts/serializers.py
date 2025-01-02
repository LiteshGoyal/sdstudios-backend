from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['email']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username','password','profile']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self,validated_data):
        profile_data = validated_data.pop('profile',{})
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        models.Profile.objects.filter(user=user).update(**profile_data)

        return user
    
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
