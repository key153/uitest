# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import logging


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
