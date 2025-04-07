from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import CustomUser


class CustomUserserializer(serializers.ModelSerializer):
    """
    creating a customuser serializer
    """

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]


class CustomUserserializerWithoutid(serializers.ModelSerializer):
    """
    creating a serializer without ID
    """

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]


class UserTodoStatsSerializer(serializers.ModelSerializer):
    """
    create a serializer which show the pending and completed count
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


class CustomUserSerializerTodoWithoutID(serializers.ModelSerializer):
    """
    CustomUserSerializer excludes ID
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


class UserPendingTodoStatsSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]


class CustomUserWithProjectStatus(serializers.ModelSerializer):
    """
    User serializer which includes count of projects of different status of which the user is part of.
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
