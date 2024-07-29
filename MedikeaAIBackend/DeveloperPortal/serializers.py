from rest_framework.serializers import ModelSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import *
from .models import *

class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class UserApiSerializer(ModelSerializer):
    class Meta:
        model = UserApi
        fields = '__all__'
    
    def validate(self, data):
        phone_number = data.get("phone_number", "")
        hospital = data.get("hospital", "")
        if not (phone_number and hospital):
            raise serializers.ValidationError("Phone number or hospital are required.")
        developer = Developer.objects.filter(phone_number=phone_number, hospital=hospital)

        if developer.exists():
            raise serializers.ValidationError("Invalid phone number or hospital.")
        
        data['developer'] = developer.first()
        return data