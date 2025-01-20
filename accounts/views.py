from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password

class SignUpView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "User created successfully"}, status=status.HTTP_201_CREATED)

class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f"Attempting login for username: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "message": "Sign in successful"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SignOutView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
            return Response({"message": "Sign out successful"}, status=status.HTTP_200_OK)

        return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    return Response({
        "username": request.user.username,
        "email": request.user.email,
    })

class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        """
        GET method to retrieve the current user's information (username and email).
        """
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email
        })

    def put(self, request):
        """
        PUT method to update the current user's username or password.
        """
        user = request.user

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username:
            user.username = username
        
        if password:
            try:
                validate_password(password)
                user.set_password(password)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        user.save()
        return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)