# coding=utf-8
import time
import unittest
from loguru import logger
from public.send_request import SendRequest
from config.basic_config import ConfigInit
# from testcase.test_login import Login


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.url = ConfigInit.login_url
        self.headers = {'Content-Type': 'application/json'}
        logger.info('############################### START ###############################')


    def tearDown(self):
        logger.info('###############################  End  ###############################')


class MyTokenTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    @classmethod
    def login_func(cls, account='xxx', pw='xxx'):
        """封装登陆函数"""
        send_data = {
            "service_id":"5e183e6f663f0000210032dc",
            "account":account,
            "password":pw}
        url = ConfigInit.login_url + '/login/login'
        headers = {'Content-Type': 'application/json'}
        r = SendRequest().send_json_post(url=url, dict=send_data, header=headers)
        token = r['data']['access_token']
        return token

    @classmethod
    def setUpClass(cls):
        cls.token = cls.login_func()

    def setUp(self):
        self.url = ConfigInit.url
        self.headers = {'Content-Type': 'application/json',
                        'Authorization':'Bearer ' + self.token
                        }
        logger.info('############################### START ###############################')


    def tearDown(self):
        time.sleep(1)
        logger.info('###############################  End  ###############################')

    def replace_dict(self, d, parameter1, parameter2):
        #替换字典中指定value
        new = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = self.replace_dict(v, parameter1, parameter2)
            if v == parameter1:
                new[k] = parameter2
            else:
                new[k] = v
        return new

    @classmethod
    def tearDownClass(cls):
        pass