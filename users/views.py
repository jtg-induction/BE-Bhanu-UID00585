from rest_framework import status

from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView


from users.serializers import UserRegistrationSerializer 

class UserRegistrationAPIView(CreateAPIView):
  serializer_class=UserRegistrationSerializer
  permission_classes=[AllowAny]



class UserLoginAPIView:
    """
    success response format
     {
       auth_token: ""
     }
    """
