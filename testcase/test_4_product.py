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
class Product(mytest.MyTokenTest):
    """设备产品模块的接口"""

    @data(*get_test_case_data(data_info, 'add_product'))
    def test_001_add_project(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        code = fake_en.word() + str(random.randint(1,1000))
        name = fake.word() + str(random.randint(1,1000)) + '- 产品'
        send_data = data["send_data"]
        send_data = self.replace_dict(send_data, '#code', code)
        send_data = self.replace_dict(send_data, '#name', name)
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

    @data(*get_test_case_data(data_info, 'get_product_list'))
    def test_002_get_product_list(self, data):
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
    @data(*get_test_case_data(data_info, 'get_product_detail'))
    def test_003_get_product_detail(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + product_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'enable_product'))
    def test_004_enable_product(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        project_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + project_id # 组成Url
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

    @data(*get_test_case_data(data_info, 'get_category_list'))
    def test_005_get_category_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        industry_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + industry_id # 组成Url
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

    @data(*get_test_case_data(data_info, 'get_category_ids'))
    def test_006_get_categoryids(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        category_ids = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + category_ids # 组成Url
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

    @data(*get_test_case_data(data_info, 'save_functions'))
    def test_007_save_functions(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        product_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = product_list_data['data'][0]['id']  # 取出依赖Id
        categoryids = get_specific_num(num=rely_num[1]-1)
        normal = [categoryids['data'][0]['id']]
        lis = [product_id, normal]
        keys = ['#id', '#normal']
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
