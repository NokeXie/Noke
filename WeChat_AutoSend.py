# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from wxpy import *  # 导入微信模块
import requests
import xlrd
import datetime
import time

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


def time_load():
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_year = now_time.date().year
    next_month = now_time.date().month
    next_day = now_time.date().day
    # 获取明天18点时间
    next_time = datetime.datetime.strptime(
        str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 18:00:00", "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天18点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time


def send_news():
    try:
        if time_load() >=0:
            print("等待%d秒后进行执行"% time_load())
            time.sleep(time_load())
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
        else:
            dayOfWeek = datetime.datetime.now().weekday()
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
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
            elif select_file() is None or (select_file()[0] == "" and select_file()[1] == ""):
                print("明天无人值班")
                send_time()
            elif select_file() is not None and select_file()[0] != "" and select_file()[1] == "":
                print("明天天腾无人值班")
                my_friend = bot.friends().search(select_file()[0])[0]
                my_friend.send(contents[0])
                my_friend.send(contents[1])
                my_friend.send(u"微信自动提醒：请留意明天值班，祝您度过美好的一天！！")
                print("天润人员值班提醒发送成功！！明天值班人员为%s" % my_friend)
                send_time()
            elif select_file() is not None and select_file()[0] == "" and select_file()[1] != "":
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


if __name__ == "__main__":
    send_news()




