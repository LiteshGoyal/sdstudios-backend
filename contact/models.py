from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField()
    email = models.EmailField()
    mobile = models.BigIntegerField()
    message = models.TextField()
