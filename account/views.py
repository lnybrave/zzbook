# -*- coding=utf-8 -*-
from rest_framework import mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import GenericViewSet

from account.models import User
from account.serializers import AvatarSerializer


class AvatarViewSet(mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AvatarSerializer
    parser_classes = (MultiPartParser,)
