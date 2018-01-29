#-*-coding=utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import os,sys
import HTMLTestRunner
import unittest, doctest
import all_case_list

# caselist=os.listdir(sys.path[0]+'\\test_case')
# for a in caselist:
	# s=a.split('.')[1:][0] #选取所要执行的用例
	# if s=='py':
		#此处执行 dos 命令并将结果保存到 log.txt
		# os.system('python '+sys.path[0]+'\\test_case\\'+a+' 1>> log.txt 2>&1')

alltestnames = all_case_list.caselist()
suite = unittest.TestSuite()
if __name__ == '__main__':
	for test in alltestnames:
		print "test:%s"%test
		suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

# suite = doctest.DocTestSuite()
# suite.addTest(unittest.makeSuite(webtest.Webtest))

filename = 'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title='Report_title',
description='Report_description')
runner.run(suite)