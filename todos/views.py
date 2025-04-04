from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.serializers import (
    TodoCreateSerializer,
    TodoUpdateSerializer,
)


class TodoAPIViewSet(ModelViewSet):
    """
    ViewSet for handling CRUD of Todos.
    """

    authentication_classes = [TokenAuthentication]
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
            return TodoUpdateSerializer
