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
class Device(mytest.MyTokenTest):
    """设备管理模块的接口"""

    @data(*get_test_case_data(data_info, 'add_device'))
    def test_001_add_device(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        code = fake_en.word() + '-' + str(random.randint(1,10000))
        send_data = data["send_data"]
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        product_id = res_data['data'][0]['id']
        lis = [code, product_id]
        keys = ['#code', '#product_id']
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

    @data(*get_test_case_data(data_info, 'device_list'))
    def test_002_device_list(self, data):
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

    @data(*get_test_case_data(data_info, 'device_detail'))
    def test_003_device_detail(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        device_code = res_data['data'][0]['code']  # 取出依赖Id
        url = self.url + url + device_code  # 组成Url
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

    @data(*get_test_case_data(data_info, 'event_log'))
    def test_004_event_log(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        device_code = res_data['data'][0]['code']  # 取出依赖Id
        url = self.url + url + device_code # 组成Url
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

    @data(*get_test_case_data(data_info, 'delete_device'))
    def test_005_delete_device(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        code = res_data['data'][1]['code']  # 取出依赖Id
        codes = []
        codes.append(code)
        url = self.url + url
        send_data = self.replace_dict(send_data, "#codes", codes)
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

    @data(*get_test_case_data(data_info, 'add_group'))
    def test_006_add_group(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        group_name = fake.word() + str(random.randint(1,100)) + '组'
        url = self.url + url
        send_data = self.replace_dict(send_data, '#name', group_name)
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

    @data(*get_test_case_data(data_info, 'group_list'))
    def test_007_group_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
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

    @data(*get_test_case_data(data_info, 'group_add_device'))
    def test_008_group_add_device(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        group_list_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        group_id = group_list_data['data'][-1]['id']  # 取出依赖Id
        device_list_data = get_specific_num(num=rely_num[1]-1)
        ids = []
        for i in range(2):
            ids.append(device_list_data['data'][i]['code'])
        lis = [group_id, ids]
        keys = ['#group_id', '#device_ids']
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

    @data(*get_test_case_data(data_info, 'group_detail'))
    def test_009_group_detail(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        id = res_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url +id
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

    @data(*get_test_case_data(data_info, 'group_device_list'))
    def test_010_group_device_list(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        id = res_data['data'][-1]['id']  # 取出依赖Id
        url = self.url + url +id
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