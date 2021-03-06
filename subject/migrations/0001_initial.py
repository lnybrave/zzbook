# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import utils.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u540d\u79f0')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001')),
                ('icon', models.ImageField(blank=True, null=True, storage=utils.storage.ImageStorage(), upload_to=b'icons/')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('del_flag', models.IntegerField(default=0, verbose_name='\u5220\u9664')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='subject.Classification')),
            ],
            options={
                'db_table': 't_classification',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='ClassificationConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Classification', verbose_name='\u5206\u7c7b')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_classification_config',
                'verbose_name': '\u5206\u7c7b\u914d\u7f6e',
                'verbose_name_plural': '\u5206\u7c7b\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('desc', models.CharField(max_length=256, verbose_name='\u63cf\u8ff0')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('del_flag', models.IntegerField(default=0, verbose_name='\u5220\u9664')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_column',
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='ColumnConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Column', verbose_name='\u680f\u76ee')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_column_config',
                'verbose_name': '\u680f\u76ee\u914d\u7f6e',
                'verbose_name_plural': '\u680f\u76ee\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(default=1, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('del_flag', models.IntegerField(default=0, verbose_name='\u5220\u9664')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='subject.Ranking')),
            ],
            options={
                'db_table': 't_ranking',
                'verbose_name': '\u6392\u884c',
                'verbose_name_plural': '\u6392\u884c',
            },
        ),
        migrations.CreateModel(
            name='RankingConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Ranking', verbose_name='\u6392\u884c')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_ranking_config',
                'verbose_name': '\u6392\u884c\u914d\u7f6e',
                'verbose_name_plural': '\u6392\u884c\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u540d\u79f0')),
                ('desc', models.CharField(max_length=256, verbose_name='\u63cf\u8ff0')),
                ('type', models.IntegerField(choices=[(1, '\u5c01\u9762+\u4e66\u540d'), (2, '\u5c01\u9762+\u4e66\u540d+\u7b80\u4ecb')], default=0, verbose_name='\u7c7b\u578b')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('del_flag', models.IntegerField(default=0, verbose_name='\u5220\u9664')),
            ],
            options={
                'ordering': ('-create_time',),
                'db_table': 't_topic',
                'verbose_name': '\u4e13\u9898',
                'verbose_name_plural': '\u4e13\u9898',
            },
        ),
        migrations.CreateModel(
            name='TopicConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('status', models.IntegerField(choices=[(0, '\u5ba1\u6838'), (1, '\u4e0a\u67b6'), (2, '\u4e0b\u67b6')], default=0, verbose_name='\u72b6\u6001')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Topic', verbose_name='\u4e13\u9898')),
            ],
            options={
                'ordering': ('order',),
                'db_table': 't_topic_config',
                'verbose_name': '\u4e13\u9898\u914d\u7f6e',
                'verbose_name_plural': '\u4e13\u9898\u914d\u7f6e',
            },
        ),
        migrations.AddField(
            model_name='columnconfig',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.Topic', verbose_name=b'\xe4\xb8\x93\xe9\xa2\x98'),
        ),
        migrations.AlterUniqueTogether(
            name='topicconfig',
            unique_together=set([('item', 'book')]),
        ),
    ]
