from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.serializers import TodoCreateSerializer, TodoViewSetSerializer, TodoupdateSerializerlizer



class TodoAPIViewSet(ModelViewSet):
    
    # serializer_class = TodoViewSetSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TodoCreateSerializer
        if self.request.method == "GET":
            return TodoCreateSerializer
        if self.request.method == "PUT":
            return TodoCreateSerializer
        if self.request.method == "PATCH":
            return TodoupdateSerializerlizer
        
        





