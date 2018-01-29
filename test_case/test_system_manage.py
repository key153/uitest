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
from Lib import login, confirm, data, face_data_manage, region


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
        cls.base_url = data.LOGIN['login_address']
        cls.verificationErrors = []
        cls.accept_next_alert = True


    def test_region(self):
        #新增区域
        driver = self.driver
        logging.info('Start test: test_002')
        try:
            #新增区域
            region.add_region(driver,u'江宁')
            #检测新增区域
            self.assertTrue(confirm.is_element_text_attribute_exist(driver,'td','江宁',r'/../td','class','bs-checkbox '))
            logging.info("Finish adding region")
            time.sleep(2)
            #编辑区域
            region.edit_region(driver,u'江宁',u'小视')
            #检测编辑区域
            self.assertTrue(confirm.is_element_text_exist(driver, 'td', u"小视"))
            logging.info("Finish editing region")
            time.sleep(2)
            #删除区域
            region.delete_region(driver,u'小视')
            self.assertFalse(confirm.is_element_text_exist(driver, 'td', u"小视"))
            logging.info("Finish deleting region")
            time.sleep(2)
            logging.info('Test 002 successfully')

        except Exception, e:
            nowTime = time.strftime('test_002'+"%Y%m%d.%H.%M.%S")
            driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
            logging.info('Test 002 fail')
            logging.error(e)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.assertEqual([], cls.verificationErrors)

if __name__ == "__main__":
    unittest.main()