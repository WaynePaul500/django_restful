# -*- coding:utf-8 -*-
# @Time    : 2020/12/17 21:28
# @Author  : Wayne
# @File    : mysql_action
from pymysql import connect
import yaml


class DB():
    def __init__(self):
        print('connect db')
        # 连接数据库
        self.conn = connect(host='127.0.0.1',
                            user='root',
                            password='',
                            db='django_restful')

    def clear(self, table_name):
        print('clear db')
        clear_sql = 'truncate ' + table_name + ';'  # 清除表数据
        with self.conn.cursor() as cursor:
            cursor.execute('set foreign_key_checks=0;')  # 清除外键约束
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self, table_name, table_data):
        # print('insert data....')
        # 遍历数据
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"  # 相当于数据库表中的value
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        print(key)
        print(value)

        insert_sql = "insert into " + table_name + "("+key+")" + "values" + "("+value+")"
        print(insert_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def close(self):
        print('colse db ')
        self.conn.close()

    def init_data(self,db_data):
        print('init db..')
        for table, data in db_data.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    # db.clear('api_group'
    # user_data = {'id':1, 'username':'asd2015', 'email': 'asd@123.com'}
    # db.insert('api_user',user_data)
    # db.close()
    f = open('db_data.yaml', 'r')
    datas = yaml.load(f)
    db.init_data(datas)
