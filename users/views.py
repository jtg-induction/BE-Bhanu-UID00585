from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, GenericAPIView
from users.serializers import UserLoginSerializer, UserRegistrationSerializer

class UserRegistrationAPIView(CreateAPIView):
    """
    API view for user registration.

    This view handles the creation of a new user account. It uses the
    UserRegistrationSerializer to validate and save the user data.
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(GenericAPIView):
    """
    API view for user login.

    This view handles user authentication and token generation. It uses the
    UserLoginSerializer to validate user credentials. Upon successful login,
    it generates and returns an authentication token for the user.
    """

    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"auth_token": token.key}, status=status.HTTP_200_OK)
