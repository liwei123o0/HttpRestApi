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
from xadmin.views.website import LoginView

class LoginViewAdmin(LoginView):
    title = u'情感分析维护管理系统'


class GlobalSetting(object):
    site_title = u'情感分析维护管理系统'   #设置头标题
    site_footer = u'Copyright © 2018 西部资信'  #设置脚标题



class KeyWordXadmin(object):
    list_display = ['word', 'flag', 'create_user', "add_time"]
    search_fields = ['word', 'flag']

class StopKeyWordXadmin(object):
    list_display = ['word', 'flag', 'create_user', "add_time"]
    search_fields = ['word', 'flag']

class CREDIT_QUALITY_INDEXadmin(object):
    list_display = ['name', 'create_user', "add_time"]
    search_fields = ['name']

class AreaReKeyWordadmin(object):
    list_display = ['area', 'flag', 'create_user', "add_time"]
    search_fields = ['area', 'flag']

class SolrReKeyWordadmin(object):
    list_display = ['credit_quality', 'area', 'flag', "add_time", 'create_user']
    search_fields = ['credit_quality', 'area', 'flag']


xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)

xadmin.site.register(CREDIT_QUALITY_INDEX, CREDIT_QUALITY_INDEXadmin)
xadmin.site.register(KeyWord, KeyWordXadmin)
xadmin.site.register(StopKeyWord, StopKeyWordXadmin)
xadmin.site.register(AreaReKeyWord, AreaReKeyWordadmin)
xadmin.site.register(SolrReKeyWord, SolrReKeyWordadmin)