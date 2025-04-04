from rest_framework import serializers
from users.serializers import CustomUserSerializerWithoutID
from .models import Todo
from users.serializers import CustomUserSerializerWithoutid


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and displaying to-do items.
    """

    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source="date_created", format="%I:%M %p, %d %b, %Y")
    creator = CustomUserSerializerWithoutid(source='user', read_only=True)
    
    class Meta:
        model = Todo
        fields = ["id", "name", "status", "created_at", "creator"]

    def get_status(self, obj):
        if obj.done:
            return "Done"
        else:
            return "To Do"

class TodoPendingSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user statistics related to pending to-do items.
    """

    pending_count = serializers.IntegerField()
    
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]

class TodoDateRangeSerializer(TodoSerializer):
    """
    Serializer for displaying to-do items with date range information.
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
class TodoCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Todo items.
    """

    user_id = serializers.IntegerField(write_only=True)
    todo = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    done = serializers.BooleanField(required=False)

    class Meta:
        model = Todo
        fields = "__all__"
