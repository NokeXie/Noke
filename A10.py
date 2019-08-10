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
import shutil
def select_pdf():  #选择00开头的pdf文件
    base_dir = r'\\192.168.10.212\FileSystem\Data\ow_tro\fmd\pdf'  # 打开的网络路径
    type = "pdf"  # 文件类型
    list = os.listdir(base_dir)  # 网络路径下的文件包含文件夹和文件
    rr = re.compile("^00\w*\.%s$" % type, re.I)  # 正则表达式匹配.pdf结尾的文件
    today = datetime.date.today()  # 获取今天的时间
    filelist = []  # 新建一个列表
    list_file = []
    for i in range(0, len(list)):
        path = os.path.join(base_dir,list[i])  # 拼接路径下的文件
        if os.path.isfile(path):  # 检查是否为文件
            filelist.append(list[i])  # 文件加入到filelist列表中
    for i in range(0, len(filelist)):
        path = os.path.join(base_dir, filelist[i])  # 拼接路径下的文件

        if os.path.isdir(path):  # 检查是否为目录 是的话跳过
            continue
        if rr.search(filelist[i]):  # 过滤pdf文件
            timestamp = os.path.getmtime(path)  # 获取目录下文件的时间戳
            date = datetime.datetime.fromtimestamp(timestamp)  # 返回指定时间戳对应的时间
            date2 = date.strftime('%Y-%m-%d')  # 返回指定时间戳对应的时间 取年月日  类型字符串
            time_tuple = time.strptime(date2, "%Y-%m-%d")  # 根据指定的格式把一个时间字符串解析为时间元组
            year, month, day = time_tuple[:3]  # 赋值
            date3 = datetime.date(year, month, day)   # 表示日期，常用的属性有：year, month和day
            if today == date3:
                path = os.path.join(base_dir, filelist[i])
                list_file.append(path)
    for i in range(0, len(list_file)):
        shutil.copy(list_file[i],r"D:\PDF")  # 文件拷贝到指定存在的文件夹
        shutil.copytree(r"D:/PDF", r"D:/PDF2") #文件夹拷贝到D盘目录无需仓库PDF2文件夹
    return list_file
if __name__=="__main__":
    select_pdf()