from django.contrib.auth import get_user_model
from rest_framework import serializers


from users.models import CustomUser
from .models import Todo
from users.serializers import CustomUserserializerWithoutid


class Todoserializer(serializers.ModelSerializer):
    """
    creating a Todoserializer
    """

    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        source="date_created", format="%I:%M %p, %d %b, %Y"
    )
    creator = CustomUserserializerWithoutid(source="user", read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "name", "status", "created_at", "creator"]

    def get_status(self, obj):
        if obj.done:
            return "Done"
        else:
            return "To Do"


class UserPendingTodoStatsSerializer(serializers.ModelSerializer):
    """
    create a serializer for for pending count
    """

    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]


class Tododaterangeserializer(serializers.ModelSerializer):
    """
    create a serializers having the start and ending date
    """

    created_at = serializers.DateTimeField(
        source="date_created", format="%I:%M %p, %d %b, %Y"
    )
    creator = serializers.CharField()
    email = serializers.EmailField(source="user.email")
    status = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["id", "creator", "email", "name", "status", "created_at"]

    def get_status(self, obj):
        return "Done" if obj.done else "Pending"
