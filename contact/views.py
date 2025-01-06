from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . import serializers 
from . import models 
# Create your views here.

class ContactView(CreateAPIView):
    serializer_class = serializers.ContactSerialzer
    queryset = models.Contact.objects.all()