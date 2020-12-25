#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2020-12-14 17:18:27
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: settings_local.py


SECRET_KEY = 'ie26u*d3w)ap__t#0y+6uirp9e7c#sds*ryg(pceq!$a)&053o'

DEBUG = True

ALLOWED_HOSTS = ['*']

CUSTOM_EXPRESSION = []

CUSTOM_APPS = [
    "DjangoUeditor",
]

CUSTOM_CONFIG_HANDLER = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
           'charset': 'utf8mb4', # 使用mysql必须设置此项
           'read_default_file': '/Application/blog-config/my.cnf',
        },
    }
}

UEDITOR_SETTINGS = {
    "toolbars": {           #定义多个工具栏显示的按钮，允行定义多个
        "name1": [['source', '|', 'bold', 'italic', 'underline']],
        "name2": []
    },
    "images_upload":{
        "allow_type":"jpg,png",    #定义允许的上传的图片类型
        "max_size":"2222kb"        #定义允许上传的图片大小，0代表不限制
    },
    "files_upload":{
         "allow_type":"zip,rar",   #定义允许的上传的文件类型
         "max_size":"2222kb"       #定义允许上传的文件大小，0代表不限制
     },
    "image_manager": {
         "location": ""         #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
    }
}
