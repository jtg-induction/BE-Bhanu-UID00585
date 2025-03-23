from rest_framework import serializers
from projects.models import Project


class Projectserializers(serializers.ModelSerializer):
    existing_member_count = serializers.IntegerField()
    
    status = serializers.SerializerMethodField()
    
    class Meta:
        model=Project
        fields=['id', 'name', "status", 'existing_member_count', 'max_members']

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
        fields = ['project_name', 'done', 'max_members']

    def get_done(self, obj):
        if(obj.status == 2 ):
            return True 
        else:
            return False   


