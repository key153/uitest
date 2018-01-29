# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, logging


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