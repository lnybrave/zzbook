# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-27 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
            ],
            options={
                'db_table': 't_data',
                'verbose_name': '\u6570\u636e',
                'verbose_name_plural': '\u6570\u636e',
            },
        ),
    ]
