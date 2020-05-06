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
    def login_func(cls, account='18175516432', pw='hb123456'):
        """封装登录函数"""
        send_data = {
            "account":account,
            "password":pw,
            "login_type":1 }
        url = ConfigInit.login_url + '/id_v2_5/user/login'
        headers = {'Content-Type': 'application/json'}
        r = SendRequest().send_json_post(url=url, dict=send_data, header=headers)
        token = r['data']['token']
        user_id = r['data']['basic']['id']
        return token,user_id

    @classmethod
    def setUpClass(cls):
        cls.token, cls.user_id = cls.login_func()

    def setUp(self):
        self.url = ConfigInit.url
        self.headers = {'Content-Type': 'application/json',
                        'JK-TOKEN':self.token,
                        'JK-USER-ID': str(self.user_id)
                        }
        logger.info(self.headers)
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