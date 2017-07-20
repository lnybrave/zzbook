# !/usr/bin/python
# -*- coding=utf-8 -*-
import datetime
from django.conf.global_settings import MEDIA_URL
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from utils import storage
from utils.const import DEL_FLAG_YES, CHOICE_GENDER, CHOICE_USER_TYPE, CHOICE_DELETE


class UserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    用户表
    """
    username = models.CharField(max_length=64, unique=True, verbose_name=u'账户')
    nickname = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'昵称')
    name = models.CharField(max_length=64, verbose_name=u'姓名')
    gender = models.CharField(max_length=2, choices=CHOICE_GENDER, verbose_name=u'性别')
    birth = models.DateField(verbose_name=u'生日', blank=True, null=True)
    head = models.ImageField(upload_to='user/', storage=storage.ImageStorage(), blank=True, null=True,
                             verbose_name=u'头像')
    brief = models.CharField(max_length=256, blank=True, verbose_name=u'简介')
    type = models.CharField(max_length=1, choices=CHOICE_USER_TYPE, verbose_name=u'用户类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, choices=CHOICE_DELETE, verbose_name=u'是否删除')
    is_staff = models.BooleanField(verbose_name=u'是否是员工', default=True)
    is_active = models.BooleanField(verbose_name=u'是否激活', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    class Meta(object):  # pylint: disable=C0111
        db_table = "t_user"
        verbose_name_plural = u"用户表"
        verbose_name = u"用户表"

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def full_name(self):
        return self.get_full_name()

    # 去除修改系统预置权限的功能
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return PermissionsMixin.has_perm(self, perm=perm, obj=obj)
        if 'auth.add_permission' in perm:
            return False
        if 'auth.add_group' in perm:
            return False
        else:
            return PermissionsMixin.has_perm(self, perm=perm, obj=obj)

    # 删除头像
    def delete_head(self):
        try:
            self.head.storage.delete(self.head.name)
        except (BaseException,):
            pass

    # 逻辑删除
    def logic_del(self):
        self.del_flag = DEL_FLAG_YES
        self.save()

    # 头像图片路劲
    @property
    def get_head_img_url(self):
        if self.head:
            return "{0}{1}".format(MEDIA_URL, self.head.url)
        else:
            return ""

    def get_format_dict(self):
        m_grade_format = {"id": 0, "name": ""}
        m_class_format = {"id": 0, "name": ""}
        if self.m_grade:
            m_grade_format = self.m_grade.get_format_dict()
        if self.m_class:
            m_class_format = self.m_class.get_format_dict()
        birth_format = self.birth.strftime('%Y-%m-%d') if self.birth else ""
        return {"id": self.pk,
                "num": self.num,
                "username": self.username,
                "name": self.name,
                "sex": self.sex,
                "birth": birth_format,
                "m_grade": m_grade_format,
                "m_class": m_class_format,
                "head": self.get_head_img_url,
                "user_type": self.user_type
                }
