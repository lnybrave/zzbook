# -*- coding=utf-8 -*-
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.core.files.base import ContentFile
from rest_framework import status, generics, permissions, views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from account.models import User, EmailVerifyRecord
from account.serializers import SetUserAvatarSerializer, LoginSerializer, UserSerializer, RegistrationSerializer, \
    PasswordResetSerializer, PasswordSerializer, SetUsernameSerializer, PasswordResetConfirmSerializer, \
    ActivationSerializer, EmailVerifySerializer
from utils import public_fun


class ActionViewMixin(object):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)


class EmailVerifyView(ActionViewMixin, generics.GenericAPIView):
    """
    邮箱验证码
    """
    serializer_class = EmailVerifySerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def _action(self, serializer):
        code = public_fun.randomCode(4)
        record = EmailVerifyRecord()
        record.code = code
        record.email = serializer.data['email']
        record.type = serializer.data['type']
        record.save()
        if public_fun.send_email_code(serializer.data['email'], code):
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegistrationView(generics.CreateAPIView):
    """
    注册
    """
    serializer_class = RegistrationSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class LoginView(ActionViewMixin, generics.GenericAPIView):
    """
    登录
    """
    serializer_class = LoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def _action(self, serializer):
        if serializer.is_valid():
            data = serializer.data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None and user.is_active:
                auth_login(self.request, user)
                ret = UserSerializer(user).data
                return Response(data=ret, status=status.HTTP_200_OK)
            else:
                ret = {'detail': '用户名或密码错误'}
                return Response(data=ret, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    """
    退出
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        if request.user.is_authenticated:
            auth_logout(request)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('用户未登录', status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(ActionViewMixin, generics.GenericAPIView):
    """
    重置密码
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class PasswordResetConfirmView(ActionViewMixin, generics.GenericAPIView):
    """
    重置密码确认
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def _action(self, serializer):
        serializer.user.set_password(serializer.data['new_password'])
        serializer.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SetPasswordView(ActionViewMixin, generics.GenericAPIView):
    """
    修改密码
    """
    serializer_class = PasswordSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def _action(self, serializer):
        self.request.user.set_password(serializer.data['new_password'])
        self.request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActivationView(ActionViewMixin, generics.GenericAPIView):
    """
    用户激活
    """
    serializer_class = ActivationSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def _action(self, serializer):
        serializer.user.is_active = True
        serializer.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SetUsernameView(ActionViewMixin, generics.GenericAPIView):
    """
    修改用户名
    """
    serializer_class = SetUsernameSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def _action(self, serializer):
        user = self.request.user
        new_username = serializer.data['new_' + User.USERNAME_FIELD]

        setattr(user, User.USERNAME_FIELD, new_username)
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(generics.RetrieveUpdateAPIView):
    """
    获取、更新用户信息
    """
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = None

    def get_object(self, *args, **kwargs):
        return self.request.user


class SetUserAvatarView(generics.GenericAPIView):
    """
    修改用户头像
    """
    serializer_class = SetUserAvatarSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def post(self, request):
        user = request.user
        user.delete_head()

        avatar = request.FILES["avatar"]  # 头像图片
        data = avatar.read()
        name = public_fun.makename(avatar.name)

        user.avatar.save(name, ContentFile(data))
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
