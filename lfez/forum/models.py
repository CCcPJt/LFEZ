# -*- coding: utf-8 -*-

from django.db import models


class Activities(models.Model):

	title = models.CharField(max_length=100, verbose_name=u'标题')
	summary = models.TextField(verbose_name=u'摘要')
	content = models.TextField(verbose_name=u'正文')
	pub_time = models.DateTimeField(default=False, verbose_name=u'发布时间')
	create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True)
	kind = models.CharField(max_length=100, verbose_name=u'活动类型')
	participant = models.IntegerField(verbose_name=u'参与人数')	
