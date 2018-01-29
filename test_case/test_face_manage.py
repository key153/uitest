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
sys.path.insert(0, parentdir)
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
        cls.driver.maximize_window()  # 将浏览器最大化显示
        login.login_web(cls.driver)
        cls.base_url = data.LOGIN['login_address']
        cls.verificationErrors = []
        cls.accept_next_alert = True

    def test_facelab(self):
        # 新增人脸库
        driver = self.driver
        logging.info('Start test: test_001')
        try:
            # 新增一个人脸库
            face_data_manage.add_face_lib(driver, 'testtest')
            # 检测新增人脸库
            logging.info(confirm.is_element_text_exist(driver, 'td', "testtest"))
            self.assertTrue(confirm.is_element_text_exist(driver, 'td', "testtest"))
            logging.info("Finish adding face lib")
            time.sleep(2)
            # 编辑人脸库
            face_data_manage.edit_face_lib(driver, 'testtest', '11')
            # 检测编辑人脸库
            self.assertTrue(confirm.is_element_text_exist(driver, 'td', "testtest11"))
            logging.info("Finish editing face lib")
            time.sleep(2)
            # 删除人脸库
            face_data_manage.delete_face_lib(driver, 'testtest11')
            self.assertFalse(confirm.is_element_text_exist(driver, 'td', "testtest11"))
            logging.info("Finish deleting face lib")
            time.sleep(2)
            logging.info('Test 001 successfully')

        except Exception, e:
            nowTime = time.strftime('test_001' + "%Y%m%d.%H.%M.%S")
            driver.get_screenshot_as_file("error_image\\%s.png" % nowTime)
            logging.info('Test 001 fail')
            logging.error(e)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.assertEqual([], cls.verificationErrors)


if __name__ == "__main__":
    unittest.main()