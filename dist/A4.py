from __future__ import unicode_literals
from wxpy import *  # 导入微信模块
import requests
import smtplib
import xlrd
import datetime
import time
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from threading import Timer
def datatoday():  # 获取今天的时间 例如2019-04-03
    today = datetime.date.today()
    return today


def tomorrow():  # 获取明天的时间 例如2019-04-04
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow
data = xlrd.open_workbook(r"\\192.168.10.56\天润文件\01-综合部\12-值班工作\天润值班排班表.xlsx")
table = data.sheets()[0]  # 获取天润值班排班表.xlsx 文件的表一
nrows = table.nrows  # 获取天润值班排班表.xlsx 文件的表一的有效行数
def kkk():
    for i in range(nrows):   # 循环逐行打印
        if i == 0 or i == 1:  # 跳过第一和第二行
            continue
        k = table.row_values(i)[1:2]  # 获取第i行的第二列数值(列表形式）例如['2019-4-1']
        fmt = '%Y-%m-%d'
        time_tuple = time.strptime(k[0], fmt)   # 函数根据指定的格式（fmt）把一个时间字符串解析为时间元组(
                                                # tm_year=2019, tm_mon=4, tm_mday=29, tm_hour=0, tm_min=0,
                                                # tm_sec=0, tm_wday=0, tm_yday=119, tm_isdst=-1)
        year, month, day = time_tuple[:3]  # 元组的前3个元素赋值给 year, month, day
        a_date = datetime.date(year, month, day)  # 解析为时间对象
        if tomorrow() == a_date:  # 判断明天的日期和表一的第二列的那个时间日期相等
            k1 = table.row_values(i)[3:4]  # 获取表一的第三列的数值（列表形式）
            k2 = table.row_values(i)[4:5]
            return k1,k2
print(kkk()[0][0])
print(kkk()[1][0])