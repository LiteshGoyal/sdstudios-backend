from django.shortcuts import render
from . import models,serializers
from rest_framework.generics import CreateAPIView, ListAPIView
# Create your views here.

class CrateBlogView(CreateAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blogs.objects.all()

class ListBlogView(ListAPIView):
    serializer_class = serializers.BlogSerializer
    queryset = models.Blogs.objects.all()
