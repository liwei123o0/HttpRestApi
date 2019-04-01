#!/usr/bin/env python
# coding: utf-8
"""httpapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import xadmin
from app.views import *
from django.conf.urls import url
from django.contrib import admin

xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', xadmin.site.urls),
    url(r'^analysis/api/v1/$', analysis_solr_api),
    url(r'^index/$', index_bases),
    url(r'^index_serach/$', index_serach)
]
