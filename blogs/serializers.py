from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'subtitle', 'description', 'author', 'created_at','image']