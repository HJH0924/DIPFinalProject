# -*- coding : utf-8 -*-
# @Time : 2021/12/14 15:33
# @Author : XJH
# @File : organizations.py
# @Software : PyCharm

"""
组织结构
"""
# confirmed by hjh in Dec 26th
# modified by xjh in Dec 26th again
# 教职工类
class Employee:
    def __init__(self, id, name, code):
        self.name = name  # 教职工编号
        self.id = id  # 教职工姓名
        self.code = code  # 教职工的特征码


LOCK_RECORD = dict()  # 打卡记录字典，格式为{姓名：[时间1，时间2]}
EMPLOYEES = list()  # 全体教职工列表
MAX_ID = 0  # 目前可用的最大ID
CODE_LEN = 6  # 特征码的默认长度
WORK_TIME = ""  # 上班时间
CLOSING_TIME = ""  # 工下班时间
USERS = dict()  # 管理员账号密码


# 添加新教职工
def add(e: Employee):
    EMPLOYEES.append(e)


# 删除指定ID的教职工记录
def remove(id):
    for emp in EMPLOYEES:
        if str(id) == str(emp.id):
            EMPLOYEES.remove(emp)  # 教职工列表中删除教职工
            if emp.name in LOCK_RECORD.keys():  # 如果存在该教职工的打卡记录
                del LOCK_RECORD[emp.name]  # 删除该教职工的打卡记录
            break


# 获取新教职工的ID
def get_new_id():
    global MAX_ID  # 调用全局变量
    MAX_ID += 1  # 当前最大的ID + 1
    return MAX_ID
