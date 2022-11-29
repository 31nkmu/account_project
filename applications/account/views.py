from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, LoginSerializer


class RegisterApiView(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(f'Вы успешно зарегистрировались.'
                        f'Вам отправлено письмо с активацией',
                        status=status.HTTP_201_CREATED)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer
