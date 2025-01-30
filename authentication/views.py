from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken


# View para Login
class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(
            {
                "token_access": response.data["access"],
                "token_renovation": response.data["refresh"],
            }
        )


# View para Renovar o Token
class TokenRefreshView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("token_renovation")
            token = RefreshToken(refresh_token)
            return Response({"token_access": str(token.access_token)})
        except InvalidToken:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


# View para Logout
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("token_renovation")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Invalida o token de renovação
            return Response({"message": "Logout successful"})
        except Exception:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
