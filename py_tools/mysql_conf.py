import configparser
import os
import json
import requests


class Myconfigparser(configparser.ConfigParser):

    def optionxform(self, optionstr):
        return optionstr


def config_dict(section):
    # section为配置文件“信息块”的名字
    config = Myconfigparser()
    config.read(os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), '.env'))
    return config._sections[section]


# d = config_dict('local')
# print(d)

