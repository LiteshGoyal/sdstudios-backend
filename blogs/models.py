from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs",null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True,null=True)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    img = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title