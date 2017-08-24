# -*- coding=utf-8 -*-
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from rest_framework import mixins, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from account.models import User
from account.serializers import AvatarSerializer, UserLoginSerializer, UserSerializer


class UserLoginAPIView(APIView):
    def post(self, request):
        """
        用户登录
        """
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None and user.is_active:
                auth_login(request, user)
                ret = UserSerializer(user).data
                return Response(data=ret, status=status.HTTP_200_OK)
            else:
                ret = {'detail': '用户名或密码错误'}
                return Response(data=ret, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    def post(self, request):
        """
        用户登出
        """
        if request.user.is_authenticated:
            auth_logout(request)
            return Response('退出成功')
        else:
            return Response('用户未登录', status=status.HTTP_400_BAD_REQUEST)


class UploadAvatarAPIViewSet(mixins.CreateModelMixin,
                             GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AvatarSerializer
    parser_classes = (MultiPartParser,)
