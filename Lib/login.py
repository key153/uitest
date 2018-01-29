# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import logging, time

import data


def login_web(driver):
    try:
        logging.info('Login ...')
        time.sleep(2)
        # 登录界面
        driver.get(data.LOGIN['login_address'])
        time.sleep(2)
        # 输入用户名和密码
        user = data.LOGIN['login_user']
        driver.find_element_by_id("username").send_keys(data.LOGIN['login_user'])
        driver.find_element_by_id("password").send_keys(data.LOGIN['login_password'])
        time.sleep(2)
        # 点击登录
        driver.find_element_by_id("userlogin").click()
        time.sleep(5)
    except:
        nowTime = time.strftime('login'+"%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
        # logging.basicConfig(filename='example.log', filemode="w", level=logging.DEBUG)
        # logging.debug('This message should go to the log file')
        logging.info('Login fail')
        # logging.warning('And this, too')
        assert expression