from rest_framework import serializers
from users.models import CustomUser
from users.serializers import CustomUserSerializerWithoutID
from .models import Todo

from users.serializers import CustomUserSerializerWithoutID


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model.
    """

    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source="date_created", format="%I:%M %p, %d %b, %Y")
    creator = CustomUserSerializerWithoutID(source='user', read_only=True)
 
    class Meta:
        model = Todo
        fields = ["id", "name", "status", "created_at", "creator"]

    def get_status(self, obj):
        if obj.done:
            return "Done"
        else:
            return "To Do"

class UserPendingTodoStatsSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "pending_count"]


class Tododaterangeserializer(serializers.ModelSerializer):

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
    Serializer for handling for APIViewSet
    """

    # user_id = serializers.IntegerField(write_only=True)
    todo = serializers.CharField(
        write_only=True,
    )
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    # date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "name", "date_created", "todo"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["name"] = validated_data.pop("todo")
        print(validated_data)
        return super().create(validated_data)


class TodoUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for handling update operations on Todo.
    """

    done = serializers.BooleanField()
    name = serializers.CharField(source="todo", read_only=True)
    todo = serializers.CharField()

    class Meta:
        model = Todo
        fields = ["todo", "done", "name"]


class TodoViewSetSerializer(serializers.ModelSerializer):
    """
    Serializer for presenting Todo data in responses.
    """

    todo_id = serializers.IntegerField(source="id")
    todo = serializers.CharField(source="name")

    class Meta:
        model = Todo
        fields = ["todo_id", "todo", "done"]

class TodoCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    todo = serializers.CharField(write_only=True)

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"


