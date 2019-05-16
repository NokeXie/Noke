# -*- coding: utf-8 -*-
print("正在加载数据库数据.....")
import pandas as pd
path1= r'\\192.168.10.18\results'
path=path1+'\FOCOSERVER.dat'
data = pd.read_csv(path,header=None,skiprows=[0],sep='\s+')
#print(data)
#skiprows[a,b,c,d] abcd行不读取//// sep=‘\s+’识别切割的字符（空格，或多个空格），默认为 “，”。

while True:
    k1 = input("请输入你要查询的单号：")
    list = []
    if k1.isdigit():
        k2 = int(k1)
        for i in range(0,len(data)):
            k = int(data.iloc[i][0:1])  # 获取dat第i行的 第一列的数值
            list.append(k)
        list2 =[i for i,x in enumerate(list) if x ==k2]   # i,x代表序 号：值  i for i,x 提取其中的序号
        #print(list2)
        print("查询中请稍后....")
        if k2 not in list and (k2+1000000) not in list:
            print("没有查询到该单号！")
        elif k2 in list or (k2+1000000) in list:
            for i in list2:
                #k = int(data.iloc[i][0:1]) # 第一种取值方式
                da = data.values[i] #第二种取值方式  推荐
                if (da[0] == k2 or da[0] == k2+1000000) and da[6]!=0:
                    print("工单号：%d(%s)    时间：%s %s   代码:%s"%(da[0],da[1],da[2],da[3],da[5]))
                    print("SPH： %f (%f)" % (da[8],da[9]))
                    print("S1：  %f (%f)" % (da[11],da[12]))
                    print("S2：  %f (%f)" % (da[14], da[15]))
                    print("CYL： %f (%f)" % (da[17],da[18]))
                    print("AXIS：%f (%f)" % (da[20], da[21]))
                    print("ADD： %f (%f)" % (da[23], da[24]))
                    print("THI： %f (%f)" % (da[35], da[36]))
                    print("PSM： %f (%f)" % (da[29], da[30]))
                    print("NRSph： %f" % (da[38]))
                    print("NRCyl： %f" % (da[41]))
                    print("NRAxis：%f" % (da[44]))
                    print("*"*57)

    else:
        print("格式输入错误！")
