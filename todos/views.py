from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.serializers import TodoCreateSerializer

class TodoAPIViewSet(ModelViewSet):
    """
    A view set for managing Todo items.

    This view set provides CRUD (Create, Read, Update, Delete) operations
    for Todo items. It uses the `TodoCreateSerializer` for serializing
    the data. The view set is accessible to any user, as it allows
    unauthenticated access.
    """
    
    serializer_class = TodoCreateSerializer
    permission_classes = [AllowAny]
    queryset = Todo.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TodoCreateSerializer
        if self.request.method == "GET":
            return TodoCreateSerializer
        if self.request.method == "PUT":
            return TodoCreateSerializer
        if self.request.method == "PATCH":
            return TodoCreateSerializer
