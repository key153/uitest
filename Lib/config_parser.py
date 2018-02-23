# -*- coding: utf-8 -*-
import ConfigParser, os


def get_config_data(section, option):
    #获取config的具体数据
    config = ConfigParser.ConfigParser()
    config.read('config' + os.path.sep + 'config.ini')
    return config.get(section, option)