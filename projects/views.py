from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import permissions
from projects.models import Project, ProjectMember
from projects.serializers import ProjectUpdateMemberSerializer
from users.models import CustomUser


class ProjectMemberApiViewSet(ModelViewSet):
    """
    View Set for adding or removing users from a project.
    """

    serializer_class = ProjectUpdateMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, project_id=None):
        """Handles adding members to the project."""
        logs = {}
        project = Project.objects.get(id=project_id)
        current_members_count = project.members.count()
        user_ids = request.data.get("user_ids")
        users = CustomUser.objects.filter(id__in=user_ids).annotate(
            project_count=Count("projectmember")
        )
        user_map = {user.id: user for user in users}

        for user_id in user_ids:
            user = user_map.get(user_id)
            if not user:
                logs[user_id] = "user does not exist"
                continue
            if current_members_count >= project.max_members:
                logs[user_id] = "project reached maximum member"
                continue
            if user.project_count >= 2:
                logs[user_id] = "cannot add as user is a member in two projects"
                continue
            try:
                ProjectMember.objects.create(member=user, project=project)
                current_members_count += 1
                logs[user_id] = "Member added sucessfully"
            except IntegrityError:
                logs[user_id] = "user is already a Member"
        return Response({"logs": logs})

    def destroy(self, request, project_id=None):
        logs = {}
        project = Project.objects.get(id=project_id)
        user_ids = request.data.get("user_ids")
        for user_id in user_ids:
            try:
                user = CustomUser.objects.get(id=user_id)
                record = ProjectMember.objects.filter(member=user, project=project)
                if not record:
                    logs[user_id] = "user is not a member of the project"
                    continue
                record.delete()
                logs[user_id] = "user removed successfully"
            except CustomUser.DoesNotExist:
                logs[user_id] = "user does not exist"
        return Response({"logs": logs})
