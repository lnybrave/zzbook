# !/usr/bin/python
# -*- coding=utf-8 -*-
import uuid

from django.conf.global_settings import MEDIA_URL
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from utils.const import DEL_FLAG_YES, CHOICE_GENDER, CHOICE_USER_TYPE, CHOICE_DELETE


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
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


def scramble_avatar_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "avatar/{}.{}".format(uuid.uuid4(), extension)


class User(AbstractBaseUser, PermissionsMixin):
    """
    用户表
    """
    username = models.CharField(max_length=64, unique=True, verbose_name=u'账户')
    nickname = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'昵称')
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'姓名')
    gender = models.CharField(max_length=1, default='0', choices=CHOICE_GENDER, verbose_name=u'性别')
    birth = models.DateField(blank=True, null=True, verbose_name=u'生日')
    avatar = models.ImageField(upload_to=scramble_avatar_filename, blank=True, null=True, verbose_name=u'头像')
    brief = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'简介')
    email = models.EmailField(blank=True)
    type = models.CharField(max_length=1, default='0', choices=CHOICE_USER_TYPE, verbose_name=u'用户类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    del_flag = models.IntegerField(default=0, choices=CHOICE_DELETE, verbose_name=u'是否删除')
    is_staff = models.BooleanField(verbose_name=u'是否是员工', default=True)
    is_active = models.BooleanField(verbose_name=u'是否激活', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = "auth_user"
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
            self.avatar.storage.delete(self.head.name)
        except (BaseException,):
            pass

    # 逻辑删除
    def logic_del(self):
        self.del_flag = DEL_FLAG_YES
        self.save()

    # 头像图片路劲
    @property
    def get_avatar_img_url(self):
        if self.avatar:
            return "{0}{1}".format(MEDIA_URL, self.avatar.url)
        else:
            return ""


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(verbose_name=u"邮箱")
    type = models.CharField(verbose_name=u"验证码类型", max_length=1,
                            choices=((1, u"注册"), (2, u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", auto_now=True)

    class Meta:
        db_table = "t_email_verify"
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)
