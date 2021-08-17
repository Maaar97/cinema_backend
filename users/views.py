from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view, permission_classes

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from utils.permissions import IsAdminOrReadOnly
from .models import User
from . import serializers

@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    response = {
        'token': None
    }
    httpStatus = status.HTTP_200_OK
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        httpStatus = status.HTTP_400_BAD_REQUEST
        return Response(data=None, status=httpStatus)
    else:
        user = authenticate(request, username=email, password=password)
        if not user:
            user = User.objects.get(email=email)
            if user.is_active:
                httpStatus = status.HTTP_404_NOT_FOUND
            else:
                httpStatus = status.HTTP_423_LOCKED
        else:
            token, created = Token.objects.get_or_create(user=user)
            response['token'] = token.key
            response.update(serializers.UserSerializerRead(user).data)
    return Response(response,status=httpStatus)

class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializerRead
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        if(request.data.get('is_staff') and not request.user.is_superuser):
            return Response(data="Only a superuser can create a staff user", status=status.HTTP_401_UNAUTHORIZED)
        write_serializer = serializers.UserSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            user = write_serializer.save()
            
            read_serializer = serializers.UserSerializerRead(user)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializerRead

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            user = User.objects.get(pk=pk)
            user.deactivate()
            serializer = serializers.UserSerializerRead(user)
            return Response(data=serializer.data, status=httpStatus)
        except User.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)