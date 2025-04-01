from rest_framework import serializers
from projects.models import Project
from users.serializers import CustomUserSerializerTodoWithoutID


class Projectserializers(serializers.ModelSerializer):
    existing_member_count = serializers.IntegerField()

    status = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "status", "existing_member_count", "max_members"]

    def get_status(self, obj):
        # if obj.done:
        #     return "Done"
        # else:
        #     return "To Do"

        # if (obj.status==0|1):
        #     return("To Do")
        # else:
        #     return("Done")

        return obj.get_status_display()


class ProjectSerializerstartswithA(serializers.ModelSerializer):
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
        
          


class ProjectReportSerializer(Projectserializers):
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
