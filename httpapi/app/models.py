#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from django.db import models
import uuid


class CREDIT_QUALITY_INDEX(models.Model):
    id = models.UUIDField(verbose_name='指标ID',primary_key=True,max_length=32)
    name = models.CharField(verbose_name='指标名', max_length=100)
    template_gid = models.UUIDField(verbose_name='指标分类ID', max_length=32)
    template_id = models.UUIDField(verbose_name='指标模板ID', max_length=32)
    add_time = models.DateField(verbose_name='添加时间')
    create_user = models.CharField(verbose_name='创建者', max_length=50)

    class Meta:
        verbose_name = '指标库维护'
        verbose_name_plural = '指标库维护'

    def __str__(self):
        return self.name

class KeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(verbose_name='关键词', max_length=50)
    add_time = models.DateField(verbose_name='添加时间')
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name='指标',
                                       on_delete=models.CASCADE, blank=True, null=True)
    create_user = models.CharField(verbose_name='创建者', max_length=50)

    class Meta:
        verbose_name = '关键词库维护'
        verbose_name_plural = '关键词库维护'

    def __str__(self):
        return self.word

class StopKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(verbose_name='停用词', max_length=50)
    add_time = models.DateField(verbose_name='添加时间')
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name='指标',
                                       on_delete=models.CASCADE, blank=True, null=True)
    create_user = models.CharField(verbose_name='创建者', max_length=50)

    class Meta:
        verbose_name = '停用关键词库维护'
        verbose_name_plural = '停用关键词库维护'

    def __str__(self):
        return self.word

class AreaReKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.CharField(verbose_name='地区', max_length=50)
    word_re = models.TextField(verbose_name='区域表达式')
    add_time = models.DateField(verbose_name='添加时间')
    create_user = models.CharField(verbose_name='创建者', max_length=50)

    class Meta:
        verbose_name = '区域表达式维护'
        verbose_name_plural = '区域表达式维护'

    def __str__(self):
        return self.area

class SolrReKeyWord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credit_quality = models.ForeignKey(CREDIT_QUALITY_INDEX, verbose_name='指标',
                                       on_delete=models.CASCADE, null=True)
    word_re = models.TextField(verbose_name='关键词表达式', null=True, blank=True)
    area = models.ForeignKey(AreaReKeyWord, verbose_name='区域',
                                       on_delete=models.CASCADE, null=True)
    area_re = models.TextField(verbose_name='区域表达式', null=True, blank=True)
    add_time = models.DateField(verbose_name='添加时间')
    create_user = models.CharField(verbose_name='创建者', max_length=50)

    class Meta:
        verbose_name = 'Solr匹配模型维护库'
        verbose_name_plural = 'Solr匹配模型维护库'

