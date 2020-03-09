#coding=utf-8
import xlrd,sys
import os
import ast
from config.basic_config import ConfigInit
from config import globalparam
# from pprint import pprint
from xlutils.copy import copy
from loguru import logger
import json
from pprint import pprint


PATH = os.path.join(globalparam.data_path, ConfigInit.data_filename)  # 运行配置
# PATH = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), 'data\\testdata', ConfigInit.data_filename)  # 调试路径
write_path = os.path.join(globalparam.project_path,'data\\testdata', ConfigInit.data_filename)
# write_path = 'D:\\workhome\\project\\apitest\\public\\data\\testdata\\data.xlsx'


# print(PATH)
def get_excel_dict(path, index=0):
    paralList=[]
    workbook=xlrd.open_workbook(path) # 打开文件
    sheet=workbook.sheets()[index]  # sheet索引从0开始
    firstRowDataList=sheet.row_values(0)#第一行数据
    #print firstRowDataList
    for rownum in range(1, sheet.nrows):#循环每一行数据
        list = sheet.row_values(rownum)
        #print type(list[3])
        dict={}
        dictTestCaseName={}

        for caseData in list:
            dict['rownum'] = rownum  # 存储当前行数，以便返回数据写入
            dict[firstRowDataList[list.index(caseData)]] =caseData #每一行数据与第一行数据对应转为字典
            #json.dumps(json.loads(caseData), ensure_ascii=False)
        # print(list)
        dictTestCaseName[list[0]]=dict#转为字典后与用例名字对应转为字典
        paralList.append(dictTestCaseName)#将处理后的数据放入列表里
    return (paralList)


def get_test_case_data(data_info,testCaseName):
    testData = data_info
    getTestCaseDataList = []
    for data in testData:
        if (list(data.keys())[0]) == testCaseName:
            getTestCaseDatadict = {}
            if data[testCaseName]['send_data']:
                getTestCaseDatadict['send_data'] = ast.literal_eval(data[testCaseName]['send_data']) # 获取表中的send_data，即接口发送数据
            else:
                getTestCaseDatadict['send_data'] = None
            getTestCaseDatadict['assert_info'] = ast.literal_eval(data[testCaseName]['assert_info']) # 获取表中的assert_info，即断言数据
            getTestCaseDatadict['method'] = data[testCaseName]['method'] # 获取表中method，即请求方式
            getTestCaseDatadict['url'] = data[testCaseName]['url'] #  获取表中url
            getTestCaseDatadict['case_name'] = data[testCaseName]['case_name'] # 获取表中case_name，即用例名称
            getTestCaseDatadict['rownum'] = data[testCaseName]['rownum'] # 获取当前数据行数，以便写入返回值
            if data[testCaseName]['rely'] == 'yes':
                #获取依赖接口的行数
                rely_num = []
                for i in eval(data[testCaseName]['num']):
                    rely_num.append(int(i))
                getTestCaseDatadict['rely_num'] = rely_num
            getTestCaseDataList.append(getTestCaseDatadict)
    return getTestCaseDataList

def write_res(rownum,data):
    #将接口返回值写入文件，res_data
    oldwb = xlrd.open_workbook(write_path, formatting_info=True)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    sheet.write(rownum, 6, data)
    newwb.save(write_path)

def get_specific_num(path=PATH, index=0, num=1):
    #获取文件指定行的res_data(获取返回接口数据)
    workbook = xlrd.open_workbook(path)  # 打开文件
    sheet = workbook.sheets()[index]
    list = sheet.row_values(num)
    print(type(list[6]))
    data = json.loads(list[6])
    return data

data_info = get_excel_dict(PATH)
# print(data_info[5])
# a = get_test_case_data(data_info, 'enable_project')
# pprint(a)
#

