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
class Configuration(mytest.MyTokenTest):
    """配置管理模块的接口"""

    @data(*get_test_case_data(data_info, 'add_industry'))
    def test_001_add_industry(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        name = fake.word() + str(random.randint(1,10000)) + '行业'
        send_data = data["send_data"]
        send_data = self.replace_dict(send_data, "#name", name)
        assert_info = data['assert_info']
        rownum = data['rownum']
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'industry_list'))
    def test_002_industry_list(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        send_data = data["send_data"]
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

    @data(*get_test_case_data(data_info, 'add_category'))
    def test_003_add_category(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        industry_id = res_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url  # 组成Url
        send_data = data['send_data']
        name = fake.word() + str(random.randint(1,10000)) + '品类'
        lis = [industry_id, name]
        keys = ['#industry_id', '#name']
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
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'category_list'))
    def test_004_category_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        industry_id = app_list['data'][-1]['id']  # 取出依赖Id)
        url = self.url + url + industry_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'delete_category'))
    def test_005_delete_category(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        category_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        category_id = category_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url + category_id  # 组成Url
        # logger.info(send_data)
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'delete':
            r = SendRequest().delete_request(url=url, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'edit_industry'))
    def test_006_edit_industry(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        industry_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        industry_id = industry_list['data'][-1]['id']  # 取出依赖Id
        url = self.url + url  # 组成Url
        name = "脚本修改" + fake.word() + str(random.randint(1,1000)) + "行业"
        lis = [industry_id, name]
        keys = ['#industry_id', '#name']
        for i in range(len(lis)):
            send_data = self.replace_dict(send_data, keys[i], lis[i])
        # logger.info(send_data)
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

    @data(*get_test_case_data(data_info, 'delete_industry'))
    def test_007_delete_industry(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        industry_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        industry_id = industry_list['data'][-1]['id']  # 取出依赖Id
        url = self.url + url + industry_id  # 组成Url
        # logger.info(send_data)
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'delete':
            r = SendRequest().delete_request(url=url, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'add_component'))
    def test_008_add_component(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        name = fake.word() + str(random.randint(1,10000)) + '类目'
        send_data = data["send_data"]
        send_data = self.replace_dict(send_data, "#name", name)
        assert_info = data['assert_info']
        rownum = data['rownum']
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'component_list'))
    def test_009_component_list(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        send_data = data["send_data"]
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

    @data(*get_test_case_data(data_info, 'edit_component'))
    def test_010_edit_component(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        component_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        component_id = component_list['data'][-1]['id']  # 取出依赖Id
        url = self.url + url  # 组成Url
        name = fake.word() + str(random.randint(1,10000)) + '类目'
        lis = [component_id, name]
        keys = ['#component_id', '#name']
        for i in range(len(lis)):
            send_data = self.replace_dict(send_data, keys[i], lis[i])
        # logger.info(send_data)
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

    @data(*get_test_case_data(data_info, 'delete_component'))
    def test_011_delete_component(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        component_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        component_id = component_list['data'][-1]['id']  # 取出依赖Id
        url = self.url + url + component_id  # 组成Url
        # logger.info(send_data)
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'delete':
            r = SendRequest().delete_request(url=url, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])



