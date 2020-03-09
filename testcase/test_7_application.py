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
class AppLication(mytest.MyTokenTest):
    """应用管理模块的接口"""

    @data(*get_test_case_data(data_info, 'add_application'))
    def test_001_add_application(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        name = fake.word() + '应用' + str(random.randint(1,10000))
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

    @data(*get_test_case_data(data_info, 'application_list'))
    def test_002_application_list(self, data):
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

    @data(*get_test_case_data(data_info, 'application_detail'))
    def test_003_application_detail(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        application_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + application_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'auth_product'))
    def test_004_auth_product(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        product_list = get_specific_num(num=rely_num[1] - 1)
        products = []
        for i in range(2):
            products.append(product_list['data'][i]['id'])
        url = self.url + url  # 组成Url
        lis = [app_id, products]
        keys = ['#app_id', '#products']
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

    @data(*get_test_case_data(data_info, 'add_menu'))
    def test_005_add_menu(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url  # 组成Url
        name = "脚本" + fake.word() + str(random.randint(1,1000)) + "管理"
        menu_url = fake.url()
        lis = [app_id, name, menu_url]
        keys = ['#appid', '#name', '#url']
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

    @data(*get_test_case_data(data_info, 'add_menu'))
    def test_005_add_menu(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url  # 组成Url
        name = "脚本" + fake.word() + str(random.randint(1,1000)) + "管理"
        menu_url = fake.url()
        lis = [app_id, name, menu_url]
        keys = ['#app_id', '#name', '#url']
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

    @data(*get_test_case_data(data_info, 'menu_list'))
    def test_006_menu_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url + app_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'first_menu_add'))
    def test_007_first_menu_add(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        parent_list = get_specific_num(num=rely_num[1] - 1)
        parent_id = parent_list['data'][0]['id']
        url = self.url + url  # 组成Url
        name = "脚本" + fake.word() + str(random.randint(1,1000)) + "二级"
        menu_url = fake.url()
        lis = [app_id, name, menu_url, parent_id]
        keys = ['#app_id', '#name', '#url', '#parent_id']
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

    @data(*get_test_case_data(data_info, 'first_menu'))
    def test_008_first_menu(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        menu_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        menu_id = menu_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url + menu_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'app_product_list'))
    def test_009_app_product_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url + app_id  # 组成Url
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

    @data(*get_test_case_data(data_info, 'enable_app'))
    def test_010_enable_app(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        app_list = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        app_id = app_list['data'][0]['id']  # 取出依赖Id
        url = self.url + url + app_id  # 组成Url
        assert_info = data['assert_info']
        rownum = data['rownum']
        # logger.info(self.headers)
        if method == 'patch':
            r = SendRequest().patch_request(url=url, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False))  # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])


