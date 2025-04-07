from rest_framework import serializers
from projects.models import Project, ProjectMember
from users.serializers import CustomUserSerializerTodoWithoutID


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model.
    """

    existing_member_count = serializers.IntegerField()

    status = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "status", "existing_member_count", "max_members"]

    def get_status(self, obj):
        return obj.get_status_display()



class ProjectSerializerStartsWithA(serializers.ModelSerializer):
    """
    serilaizer for project where the name start with A or ends with A
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
    Serilaizer for Project model which  includes specials fields.
    """

    status = serializers.SerializerMethodField()
    existing_member_count = serializers.IntegerField()
    report = CustomUserSerializerTodoWithoutID(many=True)

    class Meta:
        read_only_fields = [
            "report",
            "existing_member_count",
        ]

    def get_status(self, obj):
        return obj.get_status_display()


class ProjectReportSerializer(serializers.ModelSerializer):
    """
    Serializer that displays additional 'report' field.
    """

    report = CustomUserSerializerTodoWithoutID(many=True)
    project_title = serializers.CharField(source="name")
    class Meta:
        model = Project
        fields = ["project_title", "report"]


class ProjectUpdateMemberSerializer(serializers.ModelSerializer):
    """
    Serializer that handles adding and removing users from a project.
    """

    user_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True,
    )

    class Meta:
        model = ProjectMember
        fields = ["user_ids"]
