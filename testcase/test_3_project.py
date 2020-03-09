# coding=utf-8
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
class Project(mytest.MyTokenTest):
    """项目管理模块的接口"""

    @data(*get_test_case_data(data_info, 'add_project'))
    def test_001_add_project(self, data):
        method = data['method']
        url = data['url']
        url = self.url + url
        name = "脚本修改" + fake.word() + str(random.randint(1,1000)) + "项目"  #生成随机Name
        email = fake.email()   #生成随机email
        company = fake.company() + str(random.randint(1,1000))  #生成随机公司
        lis = [name, email, company]
        keys = ['#name', '#account', '#company']
        send_data = data["send_data"]
        for i in range(3):
            send_data = self.replace_dict(send_data, keys[i], lis[i])   #替换请求值
        logger.info(send_data)
        assert_info = data['assert_info']
        rownum = data['rownum']   #获取当前接口所在行数
        # logger.info(self.headers)
        if method == 'post':
            r = SendRequest().send_json_post(url=url, dict=send_data, header=self.headers)
        if method == 'get':
            r = SendRequest().send_get_request(url=url, header=self.headers)
        # print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url,method, send_data, r))
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'get_project_list'))
    def test_002_get_project_list(self, data):
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
        write_res(rownum, json.dumps(r, indent=2, ensure_ascii=False)) # 写入返回值
        self.assertEqual(r['code'], assert_info['code'])
        self.assertEqual(r['msg'], assert_info['msg'])

    @data(*get_test_case_data(data_info, 'modify_project'))
    def test_003_modify_project(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        assert_info = data['assert_info']
        send_data = data['send_data']
        name = res_data['data'][0]['name']
        company = res_data['data'][0]['company']
        linkman = fake.name()
        contact = fake.phone_number()
        lis = [product_id, name, company, linkman, contact]
        keys = ['#id', '#name', '#company', '#linkman', '#contact']
        for i in range(len(lis)):
            send_data = self.replace_dict(send_data, keys[i], lis[i])
        url = self.url + url
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

    @data(*get_test_case_data(data_info, 'get_project_detail'))
    def test_004_get_project_detail(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        project_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + project_id  # 组成Url
        send_data = data['send_data']
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

    @data(*get_test_case_data(data_info, 'modify_domain'))
    def test_005_modify_domain(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url   # 组成Url
        send_data = self.replace_dict(data['send_data'], '#id', product_id)
        logger.info(send_data)
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

    @data(*get_test_case_data(data_info, 'enable_project'))
    def test_006_enable_project(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url   # 组成Url
        send_data = self.replace_dict(data['send_data'], '#id', product_id)
        logger.info(send_data)
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

    @data(*get_test_case_data(data_info, 'update_pw'))
    def test_007_update_pw(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url   # 组成Url
        send_data = self.replace_dict(data['send_data'], '#id', product_id)
        logger.info(send_data)
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

    @data(*get_test_case_data(data_info, 'get_org_id'))
    def test_008_get_org_id(self, data):
        method = data['method']
        url = data['url']
        send_data = data['send_data']
        rely_num = data['rely_num']  # 依赖接口所在行数
        res_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + product_id   # 组成Url
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

    @data(*get_test_case_data(data_info, 'allot_device'))
    def test_009_allot_device(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        send_data = data['send_data']
        pro_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        pro_oid = pro_data['data'][0]['oid']  # 取出依赖Id
        res_data = get_specific_num(num=rely_num[1]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        product_id = res_data['data'][0]['id']  # 取出依赖Id
        device_data = get_specific_num(num=rely_num[2]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        device_code = []
        for i in range(2):
            device_code.append(device_data['data'][i]['code'])   # 取出依赖Id
        url = self.url + url   # 组成Url
        lis = [pro_oid, product_id, device_code]
        keys = ['#oid', '#pro_id', '#codes']
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

    @data(*get_test_case_data(data_info, 'unbind'))
    def test_010_unbind(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        send_data = data['send_data']
        device_data = get_specific_num(num=rely_num[0]-1)  # 找到对应行数，取出依赖接口返回值
        # logger.info(res_data)
        device_code = []
        device_code.append(device_data['data'][0]['code'])   # 取出依赖Id
        url = self.url + url   # 组成Url
        send_data = self.replace_dict(send_data, '#codes', device_code)
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

    @data(*get_test_case_data(data_info, 'component_empower'))
    def test_011_component_empower(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        send_data = data['send_data']
        project_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        project_id = project_data['data'][0]['id']  # 取出依赖Id
        app_list = get_specific_num(num=rely_num[1] - 1)  # 找到对应行数，取出依赖接口返回值
        app_ids = []
        for i in range(3):
            app_ids.append(app_list['data'][i]['id'])  # 取出依赖Id
        url = self.url + url  # 组成Url
        lis = [project_id, app_ids]
        keys = ['#project_id', '#app_ids']
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

    @data(*get_test_case_data(data_info, 'project_app_lis'))
    def test_012_project_app_lis(self, data):
        method = data['method']
        url = data['url']
        rely_num = data['rely_num']  # 依赖接口所在行数
        send_data = data['send_data']
        project_data = get_specific_num(num=rely_num[0] - 1)  # 找到对应行数，取出依赖接口返回值
        project_id = project_data['data'][0]['id']  # 取出依赖Id
        url = self.url + url + project_id  # 组成Url
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