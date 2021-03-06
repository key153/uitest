# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, sys, os
import HTMLTestRunner
import logging


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from Lib import login, confirm, face_data_manage, region, exceptions, config_parser


class Webtest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='log\example.log', filemode="w", level=logging.INFO)
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        # 打开chrome
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.implicitly_wait(30)
        # 将浏览器最大化显示
        cls.driver.maximize_window()
        login.login_web(cls.driver)
        cls.base_url = config_parser.get_config_data('web', 'login_web')
        cls.verificationErrors = []
        cls.accept_next_alert = True


    def test_region(self):
        #新增区域
        driver = self.driver
        logging.info('Start test: region')
        try:
            #新增区域
            region.add_region(driver,u'江宁')
            #检测新增区域
            self.assertTrue(confirm.is_element_text_attribute_exist(driver,'td','江宁',r'/../td','class','bs-checkbox '))
            self.assertTrue(confirm.is_in_database(u'江宁', 'name', 'region'))
            logging.info("Finish adding region")
            time.sleep(2)
            #编辑区域
            region.edit_region(driver,u'江宁',u'小视')
            #检测编辑区域
            self.assertTrue(confirm.is_element_text_exist(driver, 'td', u"小视"))
            self.assertFalse(confirm.is_element_text_exist(driver, 'td', u"江宁"))
            self.assertTrue(confirm.is_in_database(u'小视','name', 'region'))
            self.assertFalse(confirm.is_in_database(u'江宁', 'name', 'region'))
            logging.info("Finish editing region")
            time.sleep(2)
            #删除区域
            region.delete_region(driver,u'小视')
            self.assertFalse(confirm.is_element_text_exist(driver, 'td', u"小视"))
            self.assertFalse(confirm.is_in_database(u'小视', 'name', 'region'))
            logging.info("Finish deleting region")
            time.sleep(2)
            logging.info('Test region successfully')

        except Exception as e:
            exceptions.deal_case_error(driver, 'region', e)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.assertEqual([], cls.verificationErrors)


if __name__ == "__main__":
    unittest.main()