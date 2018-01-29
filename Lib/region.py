# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time

def add_region(driver,name):
	# 新增区域
	driver.find_element_by_xpath("//a[text()='系统管理']").click()
	time.sleep(1)
	driver.find_element_by_xpath("//a[@href='/region']").click()
	time.sleep(1)
	driver.find_element_by_xpath("//i[@class='fa fa-plus bigger-110 green']").click()
	time.sleep(1)
	driver.find_element_by_name("name").send_keys("%s"%name)
	time.sleep(1)
	driver.find_element_by_id("model_submit").click()
	time.sleep(1)
	driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
	time.sleep(1)

def edit_region(driver,name,name1):
# 编辑区域
	driver.find_element_by_xpath("//td[text()='%s']"%name).click()
	time.sleep(1)
	driver.find_element_by_xpath("//i[@class='fa fa-edit bigger-110 green']").click()
	time.sleep(1)
	driver.find_element_by_name("name").clear()
	time.sleep(1)
	driver.find_element_by_name("name").send_keys("%s"%name1)
	# time.sleep(1)
	# m=driver.find_element_by_name("parentNode.id")
	# m.find_element_by_xpath("//option[@value='1']").click()
	time.sleep(1)
	driver.find_element_by_id("model_submit").click()
	time.sleep(1)
	driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
	time.sleep(1)

def delete_region(driver,name1):
# 删除区域
	driver.find_element_by_xpath("//td[text()='%s']"%name1).click()
	time.sleep(1)
	driver.find_element_by_xpath("//i[@class='fa fa-trash bigger-110 red']").click()
	time.sleep(1)
	driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
	time.sleep(1)

def refresh_region(driver,name):
# 刷新
	driver.find_element_by_xpath("//i[@class='fa fa-refresh bigger-110 blue']").click()
	time.sleep(1)