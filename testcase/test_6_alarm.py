#coding=utf-8
import json
from public import mytest
from ddt import ddt, data, unpack
from loguru import logger
from public.send_request import SendRequest
from public.data_info import get_test_case_data, data_info, write_res, get_specific_num
from faker import Faker
import random

fake = Faker("zh_CN")
fake_en = Faker("en_US")


# import json

@ddt
class Alarm(mytest.MyTokenTest):
    """告警配置模块的接口"""

    @data(*get_test_case_data(data_info, 'add_alarm'))
    def test_001_add_alarm(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        name = fake.word() + '告警' + str(random.randint(1,10000))
        send_data = data["send_data"]
        send_data = self.replace_dict(send_data, "#name", name)
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'alarm_list'))
    def test_002_alarm_list(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        assert_info = data['assert_info']
        send_data = data['send_data']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'alarm_product_licensing'))
    def test_003_alarm_product_licensing(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        alarm_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        alarm_id = alarm_list_data['data'][-1]['id']  # 取出依赖Id
        product_list_data = get_specific_num(num=rely_num[1]-1)
        ids = []
        for i in range(random.randint(1,9)):
            ids.append(product_list_data['data'][i]['id'])
        lis = [alarm_id, ids]
        keys = ['#alarm_id', '#ids']
        for i in range(len(lis)):
            send_data = self.replace_dict(send_data, keys[i], lis[i])
        url = self.url + url
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'alarm_detail'))
    def test_004_alarm_detail(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        alarm_list_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        alarm_id = alarm_list_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url + alarm_id  # 组成Url
        send_data = data['send_data']
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'alarm_product'))
    def test_005_alarm_product(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        alarm_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        alarm_id = alarm_list_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url + alarm_id # 组成Url
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'add_alarm_rule'))
    def test_006_add_alarm_rule(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        alarm_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        alarm_id = alarm_list_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url
        alarm_ids = [alarm_id]
        name = fake.word() + " - 规则"
        code = fake_en.word() + "-" + str(random.randint(1,10000))
        lis = [name, code, alarm_ids]
        keys = ['#name', '#code', '#alarm_id']
        for i in range(len(lis)):
            send_data = self.replace_dict(send_data, keys[i], lis[i])
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'alarm_rule_list'))
    def test_007_alarm_rule_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        alarm_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        alarm_id = alarm_list_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url + alarm_id # 组成Url
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])
