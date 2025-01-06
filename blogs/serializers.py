from . import models
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = models.Blogs
        fields = ['id','title','author_username','created_at','subtitle','description','img']
        

