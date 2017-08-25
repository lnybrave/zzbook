# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 14:29
from __future__ import unicode_literals

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='\u8d26\u6237')),
                ('nickname', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u6635\u79f0')),
                ('name', models.CharField(max_length=64, verbose_name='\u59d3\u540d')),
                ('gender', models.CharField(choices=[(b'1', '\u7537'), (b'2', '\u5973')], max_length=2, verbose_name='\u6027\u522b')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=account.models.scramble_avatar_filename, verbose_name='\u5934\u50cf')),
                ('brief', models.CharField(blank=True, max_length=256, verbose_name='\u7b80\u4ecb')),
                ('type', models.CharField(choices=[(b'1', '\u5b66\u751f'), (b'2', '\u8001\u5e08')], max_length=1, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('del_flag', models.IntegerField(choices=[(1, '\u662f'), (0, '\u5426')], default=0, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_staff', models.BooleanField(default=True, verbose_name='\u662f\u5426\u662f\u5458\u5de5')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 't_user',
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
        ),
    ]
