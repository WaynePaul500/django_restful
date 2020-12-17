from django.db import models
"""
其中def __str__()的作用是美化字段的显示，方便查看。如果没有__st__方法，显示的结果是类似<__main__.Test
object at 0x0000022D6D1387B8>
"""


# 创建user表
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    groups = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# 创建group表
class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
