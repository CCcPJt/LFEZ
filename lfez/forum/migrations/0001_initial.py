# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('summary', models.TextField(verbose_name='\u6458\u8981')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('kind', models.CharField(max_length=100, verbose_name='\u6d3b\u52a8\u7c7b\u578b')),
                ('participant', models.IntegerField(verbose_name='\u53c2\u4e0e\u4eba\u6570')),
            ],
        ),
    ]
