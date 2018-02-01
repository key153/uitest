# -*- coding: utf-8 -*-
import MySQLdb
import config_parser


def connet_mysql():
    # 打开数据库连接
    db = MySQLdb.connect(host=config_parser.get_config_data('mysql', 'ip'), port=int(config_parser.get_config_data('mysql', 'port')),
                         user=config_parser.get_config_data('mysql', 'user'),passwd=config_parser.get_config_data('mysql', 'password'),
                         db=config_parser.get_config_data('mysql', 'database'), charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    return cursor


def get_count(cursor, col_name, table_name):
    # 获取数据库某表的记录条数
    cursor.execute("select count(" + col_name + ") from " + table_name)
    return cursor.fetchone()


def get_data(cursor, col_name, table_name):
    # 获取数据库某表的记录全部数据
    cursor.execute("select " + col_name + " from " + table_name)
    return cursor.fetchall()