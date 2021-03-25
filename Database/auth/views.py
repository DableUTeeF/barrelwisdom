from rest_framework.response import Response

from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView

from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

from .serializers import KnoxSerializer2, JWTSeralizer
from .utils import create_knox_token

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions

class KnoxLoginView(LoginView):

    def get_response(self):
        serializer_class = self.get_response_serializer()

        data = {
            'user': self.user,
            'token': self.token
        }
        serializer = serializer_class(instance=data, context={'request': self.request})

        return Response(serializer.data, status=200)


class KnoxRegisterView(RegisterView):

    def get_response_data(self, user):
        return KnoxSerializer2({'user': user, 'token': self.token}).data

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        self.token = create_knox_token(None, user, None)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)
        return user

class JWTObtainPairView(TokenObtainPairView):
    serializer_class = JWTSeralizer