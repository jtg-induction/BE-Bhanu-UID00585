from django.urls import path

from projects.views import ProjectMemberApiViewSet

app_name = "projects"

urlpatterns = [
    path(
        "<int:project_id>/users/",
        ProjectMemberApiViewSet.as_view(
            {"post": "create", "delete": "destroy", "get": "list"}
        ),
        name="project-member",
    )
]
