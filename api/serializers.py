# -*- coding:utf-8 -*-
# @Time    : 2020/12/13 13:07
# @Author  : Wayne
# @File    : serializers

'''
serializers用于定义api的表现形式  返回什么字段返回什么样的格式
这里序列化django自带的User和Groups
自定义User和Groups表
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # 元类
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

