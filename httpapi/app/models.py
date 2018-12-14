#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from django.db import models
import uuid
from datetime import datetime


class CREDIT_QUALITY_INDEX(models.Model):
    name = models.CharField(verbose_name=u'指标名', max_length=100, db_index=True)
    id = models.UUIDField(verbose_name=u'指标ID', primary_key=True, max_length=32)
    template_gid = models.UUIDField(verbose_name=u'指标分类ID', max_length=32)
    template_id = models.UUIDField(verbose_name=u'指标模板ID', max_length=32)
    word_re = models.TextField(verbose_name=u'指标关键词表达式')
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'指标库维护'
        verbose_name_plural = u'指标库维护'

    def __str__(self):
        return self.name


class KeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name=u'指标',
                                       on_delete=models.CASCADE, blank=True, null=True)
    word = models.CharField(verbose_name=u'关键词', max_length=50, db_index=True)
    flag = models.BooleanField(verbose_name=u'启用状态', default=True)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'关键词库维护'
        verbose_name_plural = u'关键词库维护'

    def __str__(self):
        return self.word


class StopKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name=u'指标',
                                       on_delete=models.CASCADE, blank=True, null=True)
    word = models.CharField(verbose_name=u'停用词', max_length=50, db_index=True)
    flag = models.BooleanField(verbose_name=u'启用状态', default=True)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'停用关键词库维护'
        verbose_name_plural = u'停用关键词库维护'

    def __str__(self):
        return self.word


class AreaReKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.CharField(verbose_name=u'地区', max_length=50, db_index=True)
    word_re = models.TextField(verbose_name=u'区域表达式')
    flag = models.BooleanField(verbose_name=u'启用状态', default=True)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'区域表达式维护'
        verbose_name_plural = u'区域表达式维护'

    def __str__(self):
        return self.area


class SolrReKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name=u'指标',
                                       on_delete=models.CASCADE, null=True)
    word_re = models.TextField(verbose_name=u'关键词表达式', null=True, blank=True)
    area = models.ForeignKey(AreaReKeyWord, verbose_name=u'区域',
                             on_delete=models.CASCADE, null=True)
    area_re = models.TextField(verbose_name=u'区域表达式', null=True, blank=True)
    flag = models.BooleanField(verbose_name=u'启用状态', default=True)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'Solr匹配模型维护库'
        verbose_name_plural = u'Solr匹配模型维护库'

class ClassReKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_type = models.CharField(verbose_name=u'文章类别', max_length=50, db_index=True)
    word_re = models.TextField(verbose_name=u'类别表达式')
    flag = models.BooleanField(verbose_name=u'启用状态', default=True)
    add_time = models.DateField(verbose_name=u'添加时间', default=datetime.now)
    create_user = models.CharField(verbose_name=u'创建者', max_length=50)

    class Meta:
        verbose_name = u'文章类别表达式维护'
        verbose_name_plural = u'文章类别表达式维护'

    def __str__(self):
        return self.class_type