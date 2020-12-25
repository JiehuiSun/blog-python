#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2020-12-14 17:26:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: deeru/urls_local.py


from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
from deeru.settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path(r'ueditor/',include('DjangoUeditor.urls' )),
    re_path(r'^static/ueditor/(?P<path>.*)$', serve, {'document_root': "DjangoUeditor3/DjangoUeditor/static/ueditor/"}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
