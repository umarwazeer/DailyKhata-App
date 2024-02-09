from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(generics.CreateAPIView):
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    return Response({'message': 'User successfully registered', 'data': response.data}, status=status.HTTP_201_CREATED)


class UserLoginView(generics.CreateAPIView):
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')

    user = None
    if '@' in username:
      try:
        user = CustomUser.objects.get(email=username)
      except ObjectDoesNotExist:
        pass

    if not user:
      user = authenticate(username=username, password=password)

    if user:
      refresh = RefreshToken.for_user(user)

      return Response({'refresh': str(refresh),
                       'access': str(refresh.access_token), }, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def user_logout(request):
#   if request.method == 'POST':
#     try:
#       request.user.auth_token.delete()
#       return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#     except Exception as e:
#       return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_logout(request):
  if request.method == 'POST':
    try:
      refresh_token = request.data.get('refresh_token')
      if refresh_token:
        RefreshToken(refresh_token).blacklist()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Refresh token not provided.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
