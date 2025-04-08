from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password 

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser  model.
    """

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = ["id"]

class CustomUserSerializerWithoutid(serializers.ModelSerializer):
    """
    Serializer for the CustomUser  model without the ID field.
    """

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]

class UserTodoSerializer(CustomUserSerializer):
    """
    Serializer for displaying user information along with their to-do counts.
    """

    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "completed_count",
            "pending_count",
        ]

class CustomUserSerializerTodoWithoutID(CustomUserSerializerWithoutid):
    """
    Serializer for displaying user information without the ID field, including to-do counts.
    """

    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "pending_count",
            "completed_count",
        ]

class TodoPendingSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user information along with their pending to-do count.
    """

    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class CustomUserWithProjectStatus(serializers.ModelSerializer):
    """
    Serializer for displaying user information along with project status counts.
    """

    to_do_projects = serializers.ListField(
        child=serializers.CharField(), read_only=True
    )
    in_progress_projects = serializers.ListField(
        child=serializers.CharField(), read_only=True
    )
    completed_projects = serializers.ListField(
        child=serializers.CharField(), read_only=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "to_do_projects",
            "in_progress_projects",
            "completed_projects",
        ]
