# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import logging, time

import config_parser


def login_web(driver):
    try:
        logging.info('Login ...')
        time.sleep(2)
        # 登录界面
        driver.get(config_parser.get_config_data('web', 'login_web'))
        time.sleep(2)
        # 输入用户名和密码
        driver.find_element_by_id("username").send_keys(config_parser.get_config_data('web', 'user'))
        driver.find_element_by_id("password").send_keys(config_parser.get_config_data('web', 'password'))
        time.sleep(2)
        # 点击登录
        driver.find_element_by_id("userlogin").click()
        time.sleep(5)
    except:
        nowTime = time.strftime('login'+"%Y%m%d.%H.%M.%S")
        driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
        logging.info('Login fail')
        assert expression