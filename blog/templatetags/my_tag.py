# @Time    : 2018/11/8 16:23
# @Author  : jianzheng Chang
# @Site    : 
# @File    : my_tag.py
# @Software: PyCharm Community Edition
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='tt')
def add100(v1):
    return v1 + 100