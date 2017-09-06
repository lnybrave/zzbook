# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError, transaction
from rest_framework import serializers

from account.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD, User._meta.pk.name, 'password',
        )

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                self.error_messages['cannot_create_user']
            )

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, help_text='用户名')
    password = serializers.CharField(max_length=30, help_text='密码')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    default_error_messages = {
        'email_not_found': '此邮箱未注册'
    }

    def validate_email(self, value):
        users = self.context['view'].get_users(value)
        if not users:
            raise serializers.ValidationError(
                self.error_messages['email_not_found']
            )
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        'invalid_token': '无效的token',
        'invalid_uid': '无效的uid',
    }

    # def validate_uid(self, value):
    #     try:
    #         uid = utils.decode_uid(value)
    #         self.user = User.objects.get(pk=uid)
    #     except (User.DoesNotExist, ValueError, TypeError, OverflowError):
    #         raise serializers.ValidationError(
    #             self.error_messages['invalid_uid']
    #         )
    #     return value
    #
    # def validate(self, attrs):
    #     attrs = super(UidAndTokenSerializer, self).validate(attrs)
    #     is_token_valid = self.context['view'].token_generator.check_token(
    #         self.user, attrs['token']
    #     )
    #     if is_token_valid:
    #         return attrs
    #     raise serializers.ValidationError(self.error_messages['invalid_token'])


class ActivationSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={'input_type': 'password'})

    def validate_new_password(self, value):
        validate_password(value)
        return value


class PasswordRetypeSerializer(PasswordSerializer):
    re_new_password = serializers.CharField(style={'input_type': 'password'})

    default_error_messages = {
        'password_mismatch': "密码不一致",
    }

    def validate(self, attrs):
        attrs = super(PasswordRetypeSerializer, self).validate(attrs)
        if attrs['new_password'] == attrs['re_new_password']:
            return attrs
        raise serializers.ValidationError(
            self.error_messages['password_mismatch']
        )


class CurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={'input_type': 'password'})

    default_error_messages = {
        'invalid_password': '密码无效',
    }

    def validate_current_password(self, value):
        is_password_valid = self.context['request'].user.check_password(value)
        if is_password_valid:
            return value
        raise serializers.ValidationError(
            self.error_messages['invalid_password']
        )


class SetUsernameSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            User.USERNAME_FIELD,
        )

    def __init__(self, *args, **kwargs):
        super(SetUsernameSerializer, self).__init__(*args, **kwargs)
        username_field = User.USERNAME_FIELD
        self.fields['new_' + username_field] = self.fields.pop(username_field)


class SetUserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'avatar')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
            'nickname',
            'avatar',
        )
        read_only_fields = (User.USERNAME_FIELD,)
