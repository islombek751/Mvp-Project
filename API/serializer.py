from django.db.models import fields
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from API.models import Order# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=5, write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data['email'],username = validated_data['username'],password = validated_data['password'])
        return user# User serializer
    class Meta:
        model = User
        fields = ('id','email','username','password')  
        extra_kwargs = {'password':{'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = "__all__"