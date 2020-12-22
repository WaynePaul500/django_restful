# -*- coding:utf-8 -*-
# @Time    : 2020/12/22 21:22
# @Author  : Wayne
# @File    : run
import unittest
from BSTestRunner import BSTestRunner
import time,yaml
from mysql_action import DB
import logging.config


CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


db = DB()
f = open('db_data.yaml', 'r')
# datas=yaml.load(f)
datas = yaml.load(f, Loader=yaml.FullLoader)
db.init_data(datas)


test_dir='.'
report_dir='./report'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_django_restful.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open (report_name, 'wb') as f:
    runner=BSTestRunner(stream=f, title='API Test Report', description='Django Restful生成报告')
    logging.info('=========Start API Test=============')
    runner.run(discover)