# -*- coding: utf-8 -*-
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

bot = Bot(cache_path=True)  # 微信扫描登陆，并保存缓存，下次登陆不再需要扫描


def datatoday():  # 获取今天的时间 例如2019-04-03
    today = datetime.date.today()
    return today


def tomorrow():  # 获取明天的时间 例如2019-04-04
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow


def select_file():
    data = xlrd.open_workbook(r"\\192.168.10.56\天润文件\01-综合部\12-值班工作\天润值班排班表.xlsx")
    table = data.sheets()[0]  # 获取天润值班排班表.xlsx 文件的表一
    nrows = table.nrows  # 获取天润值班排班表.xlsx 文件的表一的有效行数
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
            return k1[0],k2[0]  # 返回列表的第一个值 也就是姓名字符串

def get_news():  # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note


def send_time():
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天18点时间
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 18:00:00", "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天18点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print("微信值班提醒程序将在%d秒后自动执行" % timer_start_time)
    t = Timer(timer_start_time, send_news)
    t.start()


def send_news():
    try:
        dayOfWeek = datetime.datetime.now().weekday()
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        contents = get_news()
        if select_file()[0] == "解建国" and dayOfWeek != 2:
            bot.file_helper.send(contents[0])
            bot.file_helper.send(contents[1])
            bot.file_helper.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            print("天润人员值班提醒发送成功！！明天值班人员为解建国")
            my_friend = bot.friends().search(select_file()[1])[0]
            my_friend.send(contents[0])
            my_friend.send(contents[1])
            my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            print("天腾值班提醒发送成功！！明天值班人员为%s" % my_friend)
            send_time()
        elif select_file()[0] == "解建国" and dayOfWeek == 2:
            bot.file_helper.send(contents[0])
            bot.file_helper.send(contents[1])
            bot.file_helper.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            bot.file_helper.send(u"微信自动提醒：请留意明天是周四，安全检查勿忘记！")
            print("天润人员值班提醒发送成功！！明天值班人员为解建国")
            my_friend = bot.friends().search(select_file()[1])[0]
            my_friend.send(contents[0])
            my_friend.send(contents[1])
            my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            print("天腾值班提醒发送成功！！明天值班人员为%s" % my_friend)
            send_time()

        elif select_file()[0] != "" and select_file()[1] != "" and select_file() is not None:
            if dayOfWeek == 2:
                my_friend = bot.friends().search(select_file()[0])[0]
                my_friend.send(contents[0])
                my_friend.send(contents[1])
                my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
                my_friend.send(u"微信自动提醒：请留意明天是周四，安全检查勿忘记！")
                print("天润人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
                my_friend = bot.friends().search(select_file()[1])[0]
                my_friend.send(contents[0])
                my_friend.send(contents[1])
                my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
                print("天腾人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
                send_time()
            else:
                my_friend = bot.friends().search(select_file()[0])[0]
                my_friend.send(contents[0])
                my_friend.send(contents[1])
                my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
                print("天润人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
                my_friend = bot.friends().search(select_file()[1])[0]
                my_friend.send(contents[0])
                my_friend.send(contents[1])
                my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
                print("天腾人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
                send_time()
        elif select_file()is None or (select_file()[0] =="" and select_file()[1] ==""):
            print("明天无人值班")
            send_time()
        elif select_file() is not None and select_file()[0] !="" and select_file()[1] =="":
            print("明天天腾无人值班")
            my_friend = bot.friends().search(select_file()[0])[0]
            my_friend.send(contents[0])
            my_friend.send(contents[1])
            my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            print("天润人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
            send_time()
        elif select_file() is not None and select_file()[0] =="" and select_file()[1] !="":
            print("明天天润无人值班")
            my_friend = bot.friends().search(select_file()[1])[0]
            my_friend.send(contents[0])
            my_friend.send(contents[1])
            my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
            print("天腾人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
            send_time()
    except:

        # 你的微信名称，不是微信帐号。
        bot.file_helper.send(u"今天消息发生失败了")


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
            my_friend = bot.friends().search("胡祥军")[0]
            my_friend.send(u"这里是微信自动提醒：请留意今天FMD没有完成，下午16：20会再次尝试自动读取文件进行推送。")
            print("FMD文件不存在，下次邮件在%d秒后尝试自动推送" % Dtime16_20())
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
    send_news()
    mailsend()



