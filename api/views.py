"""
视图用于向用户展示数据
ViewSets 用于定义视图的展现形式
"""
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a user instance.(返回具体的用户实例)
    list:
    Return all users, ordered by most recently joined.(返回所有的用户实例，按照倒叙排列)
    create:
    Create a new user.（创建新用户）
    delete:
    Remove an existing user.（删除用户）
    partial_update:
    Update one or more fields on an existing user.（）
    update:
    Update a user.（更新一个用户）
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a group instance.
    list:
    Return all groups, ordered by most recently joined.
    create:
    Create a new group.
    delete:
    Remove an existing group.
    partial_update:
    Update one or more fields on an existing group.
    update:
    Update a group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer

