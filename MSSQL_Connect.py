import xlwt
import pymssql
from 读取花名册excel数据 import renyuan


class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db

    def GetConnect(self):
        if not self.db:
            raise(NameError,'没有目标数据库')
        self.connect=pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur=self.connect.cursor()
        if not cur:
            raise(NameError,'数据库访问失败')
        else:
            return cur

    def ExecSql(self,sql):
        cur=self.GetConnect()
        cur.execute(sql)
        self.connect.commit()
        self.connect.close()

    def ExecQuery(self,sql):
        cur=    self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.connect.close()
        return resList


def main():
    ms = MSSQL(host="192.168.10.77", user="sa", pwd="sa", db="STCard_Enp")
    resList = ms.ExecQuery("select *from ST_Person where Person_Name <>'外来' and Is_Del <>1 and Dept_ID <>9 and Dept_ID <>3 "
                     "and Dept_ID <>7 and Dept_ID <>8 and Card_No <>''")
    k = 0
    path = r"\\192.168.10.56\天润文件\03-财务部\17-消费系统清理人员\非在职人员名单.xls"
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("非在职人员名单")  # 在工作簿中新建一个表格
    for i in range(0,len(resList)):
        if resList[i][4] not in renyuan():
            print(resList[i][4])
            sheet.write(k, 0, resList[i][4])  # 像表格中写入数据（对应的行和列）
            k=k+1
            print(k)
            workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


if __name__ == '__main__':
    main()
    input("执行完成................!")
