#-*-coding=utf-8 -*-
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import os,sys
import HTMLTestRunner
import unittest, doctest
import all_case_list


alltestnames = all_case_list.caselist()
suite = unittest.TestSuite()
if __name__ == '__main__':
    for test in alltestnames:
        print "test:%s"%test
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))


filename = 'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title='Report_title',
description='Report_description')
runner.run(suite)