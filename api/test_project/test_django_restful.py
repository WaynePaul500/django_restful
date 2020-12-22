# -*- coding:utf-8 -*-
# @Time    : 2020/12/22 20:26
# @Author  : Wayne
# @File    : test_django_restful
import requests
import unittest
from api.test_project.mysql_action import DB
import yaml
import logging


# 登录账户
class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('pang', 'pang1234')
        # 清楚数据
        db = DB()
        f = open('db_data.yaml', 'r')
        # datas = yaml.load(f)
        datas = yaml.load(f, Loader=yaml.FullLoader)
        db.init_data(datas)

    # 查寻数据，来源于yaml文件
    def test_001_get_user(self):
        logging.info('test_001_get_user----查询用户ID为1的信息')
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'Mark-01')
        self.assertEqual(result['email'], 'Mark-01@163.com')

    # @unittest.skip('skip add user')
    def test_002_add_user(self):
        logging.info('test_002_add_user---添加用户信息')
        # 添加一个用户 ID为3，分组在第二组
        form_data = {'id': 3, 'username': 'zxw3', 'email': 'zxw3@qq.com', 'groups': 'http://127.0.0.1:8000/groups/2/'}
        r = requests.post(self.base_url + '/', data=form_data, auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'zxw3')

    # @unittest.skip('skip test_delete_user')
    def test_003_delete_user(self):
        logging.info('test_003_delete_user---删除用户信息')
        r = requests.delete(self.base_url + '/2/', auth=self.auth)
        self.assertEqual(r.status_code, 204)

    def test_004_update_user(self):
        logging.info('test_004_update_user---更新用户信息')
        form_data = {'email': 'updateMark@163.com'}
        r = requests.patch(self.base_url + '/1/', auth=self.auth, data=form_data)
        result = r.json()
        self.assertEqual(result['email'], 'updateMark@163.com')

    def test_005_no_auth(self):
        logging.info('test_005_no_auth')
        r = requests.get(self.base_url)
        result = r.json()
        self.assertEqual(result['detail'], 'Authentication credentials were not provided.')


# 分组，并登录接口
class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('pang', 'pang1234')

    def test_001_group_developer(self):
        logging.info('test_001_group_developer')
        r = requests.get(self.base_url + '/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'Developer')

    def test_002_add_group(self):
        logging.info('test_002_add_group---添加组')
        form_data = {'name': 'Pm'}
        r = requests.post(self.base_url + '/', auth=self.auth, data=form_data)
        result = r.json()
        self.assertEqual(result['name'], 'Pm')

    def test_003_update_group(self):
        logging.info('test_003_update_group---更新组')
        form_data = {'name': 'Jack-update'}
        r = requests.patch(self.base_url + '/2/', auth=self.auth, data=form_data)
        result = r.json()
        self.assertEqual(result['name'], 'Jack-update')

    def test_004_delete_group(self):
        logging.info('test_004_delete_group---删除组id为1的信息')
        r = requests.delete(self.base_url + '/1/', auth=self.auth)
        self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    db = DB()
    f = open('db_data.yaml', 'r')
    datas = yaml.load(f)
    db.init_data(datas)
    unittest.main()