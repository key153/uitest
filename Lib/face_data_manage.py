# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_face_lib(driver,name):
    # 新增一个人脸库
    driver.find_element_by_xpath("//a[text()='人脸库管理']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//i[@class='fa fa-plus bigger-110 green']").click()
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("%s"%name)
    time.sleep(1)
    driver.find_element_by_id("model_submit").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
    time.sleep(1)


def edit_face_lib(driver,name1,name2):
    # 编辑人脸库
    driver.find_element_by_xpath("//td[text()='%s']"%name1).click()
    time.sleep(1)
    driver.find_element_by_xpath("//i[@class='fa fa-edit bigger-110 green']").click()
    time.sleep(1)
    driver.find_element_by_name("name").send_keys("%s"%name2)
    time.sleep(1)
    driver.find_element_by_id("model_submit").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
    time.sleep(1)


def delete_face_lib(driver,name):
    # 删除人脸库
    driver.find_element_by_xpath("//td[text()='%s']"%name).click()
    time.sleep(1)
    driver.find_element_by_xpath("//i[@class='fa fa-trash bigger-110 red']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
    time.sleep(1)


def refresh_face_lib(driver, name):
    # 刷新人脸库
    driver.find_element_by_xpath("//i[@class='fa fa-refresh bigger-110 blue']").click()
    logging.info('11111111111111')
    logging.info(driver.find_element_by_xpath("//*[@id='table']/thead/tr/th[2]/div[1]").text)
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='table']/thead/tr/th[2]/div[1]"), 'ID'))
    # logging.info(WebDriverWait(driver, 20).until(EC.title_is(u"视频监控平台")))
    # WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='content']/div[1]/h1"), u'人脸库列表'))
    logging.info('222222222222222')
    # WebDriverWait(driver, 20).until_not(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='content']/div[4]/div[1]/div[2]/div[2]/div"), name))