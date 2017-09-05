# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('book', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='\u56fe\u4e66')),
                ('topic', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.Topic', verbose_name='\u4e13\u9898')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_recommend',
                'verbose_name': '\u7cbe\u9009',
                'verbose_name_plural': '\u7cbe\u9009',
            },
        ),
    ]
