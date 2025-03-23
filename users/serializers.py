from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import CustomUser


# Add your serializers

class CustomUserserializer(serializers.ModelSerializer):

   

    class Meta:
        model = CustomUser
        fields = ["id", "email","first_name", "last_name"]


class CustomUserserializerWithoutid(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ "email","first_name", "last_name"]


class UserTodoStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'completed_count', 'pending_count']

class UserPendingTodoStatsSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'pending_count']        


    