# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib
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
#   邮件发送部分

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
    return list_file


def Dtime16_30():  # 获取距离今天16：30分点时间，单位为秒
    now_time = datetime.datetime.now()   # 获取今天时间
    next_time = now_time
    next_year = next_time.date().year    # 获取今天时间的年
    next_month = next_time.date().month  # 获取今天时间的月
    next_day = next_time.date().day      # 获取今天时间的日
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 16:30:00", "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()    # 获取距离今天16：30分点时间，单位为秒
    return timer_start_time


def Dtime16_20():  # 获取距离今天16：20分点时间，单位为秒
    now_time = datetime.datetime.now()
    next_time = now_time
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 16:20:00", "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time


def Dtime11():  # 获取距离明天14点的时间秒数
    now_time = datetime.datetime.now()
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 14:00:00", "%Y-%m-%d %H:%M:%S")
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time


def mailsend():
    try:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        dayOfWeek = datetime.datetime.now().weekday()
        if dayOfWeek == 5:
            print("今天周六，下次邮件在下周一尝试自动推送" )
            t = Timer(Dtime11()+86400, mailsend)
            t.start()
        elif dayOfWeek == 6:
            print("今天周日，下次邮件在下周一尝试自动推送" )
            t = Timer(Dtime11(), mailsend)
            t.start()
        elif len(select_pdf()) > 0 and Dtime16_30() < 0 and dayOfWeek != 5 and dayOfWeek != 6:
            print("今天FMD文件发送时间失效，下次邮件在%d秒后尝试自动推送" % Dtime11())
            t = Timer(Dtime11(), mailsend)
            t.start()
        elif len(select_pdf()) ==0 and Dtime16_30() > 0 and dayOfWeek != 5 and dayOfWeek != 6:
            print("FMD文件不存在，下次邮件在%d秒后尝试自动推送" % Dtime16_20())
            _user = "it@troptical.com"
            _pwd = "241007s"
            _to = "444325905@qq.com"
            # _to = ["Phillip.Dietz@rodenstock.com","fmd-franchise@optovision.de"]
            # for address in _to:
            # 如名字所示Multipart就是分多个部分
            msg = MIMEMultipart()
            msg["Subject"] = "FMD未完成_" + str(datatoday())
            msg["From"] = _user
            msg["To"] = _to
            # ---这是文字部分---
            part = MIMEText(" 请留言今天FMD没有完成，今天下午16：20将再次进行读取文件发生，请尽快完成")
            msg.attach(part)
            s = smtplib.SMTP("s48.cn4e.com", timeout=300)  # 连接smtp邮件服务器,端口默认是25
            print("连接邮件服务器...")
            s.login(_user, _pwd)  # 登陆服务器
            print("登陆邮件服务器成功")
            strat_time = time.time()
            s.sendmail(_user, _to, msg.as_string())  # 发送邮件
            stop_time = time.time()
            print("FMD提醒邮件成功，耗时%d秒" % (stop_time - strat_time))
            s.close()
            time.sleep(Dtime16_20())
            if len(select_pdf()) >0:
                mailsend()
            else:
                t = Timer(Dtime11(), mailsend)
                print("今天FMD文件发送时间失效，下次邮件在%d秒后尝试自动推送" % Dtime11())
                t.start()
        elif len(select_pdf()) ==0 and Dtime16_30() < 0 and dayOfWeek != 5 and dayOfWeek != 6:
            print("今天FMD文件发送失败，下次邮件在%d秒后尝试自动推送" % Dtime11())
            t = Timer(Dtime11(), mailsend)
            t.start()
        elif len(select_pdf())>0 and dayOfWeek != 5 and dayOfWeek != 6:
            _user = "it@troptical.com"
            _pwd = "241007s"
            _to = "fmd-franchise@optovision.de"
            #_to = ["Phillip.Dietz@rodenstock.com","fmd-franchise@optovision.de"]
            #for address in _to:
            # 如名字所示Multipart就是分多个部分
            msg = MIMEMultipart()
            msg["Subject"] = "FMD_"+str(datatoday())
            msg["From"] = _user
            msg["To"] = _to
            # ---这是文字部分---
            part = MIMEText(" This is the automatic push of mail. Please do not reply.")
            msg.attach(part)
            for i in range(0, len(select_pdf())):
                # pdf类型附件
                part = MIMEApplication(open(select_pdf()[i], 'rb').read())
                msg.attach(part)
                part.add_header('Content-Disposition', 'attachment', filename="FMD_" + str(i + 1) + ".pdf")
            s = smtplib.SMTP("s48.cn4e.com", timeout=300)  # 连接smtp邮件服务器,端口默认是25
            print("连接邮件服务器...")
            s.login(_user, _pwd)  # 登陆服务器
            print("登陆邮件服务器成功")
            strat_time = time.time()
            s.sendmail(_user, _to, msg.as_string())  # 发送邮件
            stop_time = time.time()
            print("发送邮件成功，耗时%d秒"%(stop_time - strat_time))
            s.close()
            print("下次邮件在%d秒后尝试自动推送" % Dtime11())
            t = Timer(Dtime11(), mailsend)
            t.start()
    except:
        print("失败")



if __name__ == "__main__":
    mailsend()



