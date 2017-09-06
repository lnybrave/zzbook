# !/usr/bin/python
# -*- coding=utf-8 -*-
from django.conf.urls import url

from account import views
from account.models import User

urlpatterns = [
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^activate/$', views.ActivationView.as_view(), name='activate'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password/$', views.SetPasswordView.as_view(), name='set_password'),
    url(
        r'^password/reset/$',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        r'^password/reset/confirm/$',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(
        r'^{0}/$'.format(User.USERNAME_FIELD),
        views.SetUsernameView.as_view(),
        name='set_username'
    ),
    url(
        r'^me/$',
        views.UserView.as_view(),
        name='user'
    ),
    url(
        r'^me/avatar/$',
        views.SetUserAvatarView.as_view(),
        name='set_avatar'
    ),
    url(
        r'^verify/$',
        views.EmailVerifyView.as_view(),
        name='set_avatar'
    ),
]
