from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for interacting with users data.
    """

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class CustomUserSerializerWithoutID(serializers.ModelSerializer):
    """
    Serializer without id
    """

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]


class CustomUserSerializerWithTodoStats(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "pending_count",
            "completed_count",
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


class TodoPendingSerializer(serializers.ModelSerializer):
    """
    Todo with Pending Serializer
    """

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


class UserRegistrationSerializer(CustomUserSerializer):
    """
    Serializer the data in user register Api.
    """

    first_name = serializers.RegexField(
        required=False,
        regex=r"^[a-zA-Z0-9]+$",
        error_messages={"invalid": "only alphanumeric are allowed."},
    )
    last_name = serializers.RegexField(
        required=False,
        regex=r"^[a-zA-Z0-9]+$",
        error_messages={"invalid": "only alphanumeric are allowed."},
    )
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )
    token = serializers.SerializerMethodField()

    class Meta(CustomUserSerializer.Meta):
        fields = CustomUserSerializer.Meta.fields + [
            "password",
            "confirm_password",
            "token",
        ]
        read_only_fields = CustomUserSerializer.Meta.read_only_fields + ["token"]

    def get_token(self, user):
        try:
            token, _ = Token.objects.get_or_create(user=user)
            return token.key
        except Exception:
            raise serializers.ValidationError({"token": "Unable to create a token"})

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords don't match."}
            )
        return data

    def validate_password(self, password):
        try:
            validate_password(password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return password

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        return super().create(validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for handling user login.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, data):
        try:
            user = CustomUser.objects.get(email=data["email"])
            if not user.check_password(data["password"]):
                raise serializers.ValidationError("Invalid please try again.")
            data["user"] = user
            return data
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid please try again.")
