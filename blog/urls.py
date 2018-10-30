# @Time    : 2018/10/24 16:11
# @Author  : jianzheng Chang
# @Site    : 
# @File    : urls.py.py
# @Software: PyCharm Community Edition

from django.contrib import admin
from django.urls import path,include,re_path
from blog import views

urlpatterns = [
    #带参数
    path(r'^articles/2013/', views.year_2003_12,{'name':'的饭是大连贵金属'}),
    re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.current_year),
]