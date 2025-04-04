from django.contrib import admin

from projects.models import Project, ProjectMember

# class ProjectAdmin(admin.ModelAdmin):
#     list_display =


admin.site.register(Project)
admin.site.register(ProjectMember)
