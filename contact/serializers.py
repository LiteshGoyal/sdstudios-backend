from . import models
from rest_framework import serializers

class ContactSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['full_name','email','mobile','message']
