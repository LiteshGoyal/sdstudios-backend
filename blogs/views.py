from django.shortcuts import render
from . import models,serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class CrateBlogView(CreateAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blogs.objects.all()
    permission_classes = [AllowAny] 

class ListBlogView(ListAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blogs.objects.all()
    permission_classes = [AllowAny] 
