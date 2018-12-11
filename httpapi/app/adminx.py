# -*- coding: utf-8 -*-
# ! /usr/bin/env python

"""
@author:LiWei
@license:LiWei
@contact:877129310@qq.com
@version:
@var:
@note:

"""
import xadmin
from .models import *
from xadmin import views

class GlobalSetting(object):
    site_title = u'情感分析维护管理系统'   #设置头标题
    site_footer = u'西部资信'  #设置脚标题



class KeyWordXadmin(object):
    list_display = ['word', 'create_user', "add_time"]
    search_fields = ['word']

class StopKeyWordXadmin(object):
    list_display = ['word', 'create_user', "add_time"]
    search_fields = ['word']

class CREDIT_QUALITY_INDEXadmin(object):
    list_display = ['name', 'create_user', "add_time"]
    search_fields = ['name']

class AreaReKeyWordadmin(object):
    list_display = ['area', 'create_user', "add_time"]
    search_fields = ['area']

class SolrReKeyWordadmin(object):
    list_display = ['credit_quality', 'area', "add_time", 'create_user']
    search_fields = ['credit_quality', 'area']


xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(KeyWord, KeyWordXadmin)
xadmin.site.register(StopKeyWord, StopKeyWordXadmin)
xadmin.site.register(AreaReKeyWord, AreaReKeyWordadmin)
xadmin.site.register(CREDIT_QUALITY_INDEX, CREDIT_QUALITY_INDEXadmin)
xadmin.site.register(SolrReKeyWord, SolrReKeyWordadmin)