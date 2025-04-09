from django.urls import path
from todos.views import TodoAPIViewSet
from rest_framework import routers

app_name = "todos"

router = routers.SimpleRouter()
router.register(r"todos", TodoAPIViewSet, "todos")
urlpatterns = router.urls
