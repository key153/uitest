# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import mysql


def is_element_text_exist(driver,style,text):
    try:
        driver.find_element_by_xpath("//%s[text()='%s']"%(style,text))
        return True
    except:
        return False


def is_element_text_attribute_exist(driver,style1,text,style2,attribute,attribute_value):
    try:
        if driver.find_element_by_xpath("//%s[text()='%s']%s"%(style1,text,style2)).get_attribute(attribute) ==attribute_value:
            return True
    except:
        return False


def is_element_id_exist(driver,id):
    try:
        driver.find_element_by_id("%s"%id)
        return True
    except:
        return False


def id_element_name_exist(driver,name):
    try:
        driver.find_element_by_name("%s"%name)
        return True
    except:
        return False


def is_in_database(data, col_name, table_name):
    #判断数据是否在数据库内
    cursor = mysql.connet_mysql()
    mysql_data = mysql.get_data(cursor, col_name, table_name)
    list_data = []
    for i in range(len(mysql_data)):
        list_data.append(mysql_data[i][0])
    if data in list_data:
        return True
    else:
        return False