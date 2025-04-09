from rest_framework import serializers
from projects.models import Project
from users.serializers import CustomUserSerializerTodoWithoutID

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and displaying project details.
    """
    existing_member_count = serializers.IntegerField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "status", "existing_member_count", "max_members"]

    def get_status(self, obj):
        return obj.get_status_display() 

class ProjectSerializertartswithA(serializers.ModelSerializer):
    """
    Serializer for projects where the name starts with 'A'.
    """

    project_name = serializers.CharField(source="name")
    done = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["project_name", "done", "max_members"]

    def get_done(self, obj):
        if obj.status == 2:
            return True
        else:
            return False

class ProjectReportSerializer(ProjectSerializer):
    """
    Serializer that displays additional 'report' field.
    """

    report = CustomUserSerializerTodoWithoutID(many=True)
    project_title = serializers.CharField(source="name")

    class Meta:
        model = Project
        fields = ["project_title", "report"]
