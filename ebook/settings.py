#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
Django settings for ebook project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l4o_sxak#azb53qm#z^czpn*z58*6os+1l&_t4x)_n$gis_5mk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.159']

# Application definition

INSTALLED_APPS = [
    'suit',  # 必须放在admin前面
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'forms_builder.forms',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework_swagger',

    'mptt',

    'account',
    'banner',
    'books',
    'bookshelf',
    'menu',
    'subject',
    'recommend',
    'search',
    'data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ebook.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False  # Time Zone
DATETIME_FORMAT = 'Y-m-d H:i:s'  # suit在admin里设置时间的一个小bug。需要把时间格式指定一下
DATE_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))
STATIC_ROOT = os.path.join(SITE_ROOT, 'collectstatic')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# suit
SUIT_CONFIG = {
    'ADMIN_NAME': u'管理平台',
    'HEADER_DATE_FORMAT': 'Y年 F j日 l',
    'LIST_PER_PAGE': 20,
    'MENU': (
        {'app': 'account', 'label': u'用户', 'icon': 'icon-user', },
        {'app': 'banner', 'label': u'广告', 'icon': 'icon-user', },
        {'app': 'books', 'label': u'图书', 'icon': 'icon-user', },
        {'app': 'bookshelf', 'label': u'书架', 'icon': 'icon-user', },
        {'app': 'menu', 'label': u'菜单', 'icon': 'icon-user', },
        {'app': 'subject', 'label': u'频道', 'icon': 'icon-user', },
        {'app': 'recommend', 'label': u'精选', 'icon': 'icon-user', },
        {'app': 'search', 'label': u'关键字', 'icon': 'icon-user', },
        {'app': 'data', 'label': u'数据源', 'icon': 'icon-user', },
    )
}

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGE_SIZE': 20,
}

REST_SESSION_LOGIN = True

# swagger
SWAGGER_SETTINGS = {
    # 'USE_SESSION_AUTH': False,
    # 'APIS_SORTER': 'alpha',
    # 'LOGIN_URL': 'login',
    # 'LOGOUT_URL': 'logout',
}

# auth user
AUTH_USER_MODEL = 'account.User'

# default is 10 pixels
MPTT_ADMIN_LEVEL_INDENT = 20

SITE_ID = 1

FORMS_BUILDER_EXTRA_FIELDS = (
    (100, "django.forms.BooleanField", "My cool checkbox"),
)

try:
    from local_settings import *
except ImportError:
    pass
