from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import CustomUser
from .models import Todo
from users.serializers import  CustomUserserializerWithoutid

class Todoserializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source="date_created", format="%I:%M %p, %d %b, %Y")
    creator = CustomUserserializerWithoutid(source='user', read_only=True)
    
    class Meta:
        model=Todo
        fields=["id","name","status","created_at","creator"]

    def get_status(self, obj):
        if obj.done:
            return "Done"
        else:
            return "To Do"

class UserPendingTodoStatsSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'pending_count']


class Tododaterangeserializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source="date_created", format="%I:%M %p, %d %b, %Y")  
    creator = serializers.CharField() 
    email = serializers.EmailField(source="user.email") 
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['id', 'creator', 'email', 'name', 'status', 'created_at'] 

    def get_status(self, obj):
        return "Done" if obj.done else "Pending"
    

class TodoCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)  
    todo = serializers.CharField(write_only=True)  

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"

class TodoupdateSerializerlizer(serializers.ModelSerializer):
    done = serializers.BooleanField()
    name = serializers.CharField(source='todo', read_only=True) 
    todo=serializers.CharField()
    class Meta:
        model=Todo
        fields=["todo","done","name"]