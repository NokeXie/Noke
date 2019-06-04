import xlwt
import xlrd
import pymssql
data = xlrd.open_workbook(r"D:\2019花名册.xls")
table = data.sheets()[0]  # 获取天润值班排班表.xlsx 文件的表一
nrows = table.nrows  # 获取天润值班排班表.xlsx 文件的表一的有效行数
def renyuan():
    list=[]
    for i in range(nrows):   # 循环逐行打印
        if i == 0 :  # 跳过第一和第二行
            continue
        k = table.row_values(i)[1:2] # 获取第i行的第二列数值(列表形式）例如['2019-4-1']
        list.append(k[0])
    return list


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
    resList = ms.ExecQuery("select * from ST_Person where Person_Name <>'外来' and Is_Del <>1 and (Dept_ID =9 or Dept_ID =3 or Dept_ID =7 or Dept_ID =8,Dept_ID =2) and Card_No <>''")
    k = 0
    path = r"D:\非在职人员名单.xls"
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet("非在职人员名单")  # 在工作簿中新建一个表格
    for i in range(0,len(resList)):
        if resList[i][4] not in renyuan():
            sheet.write(k, 0, resList[i][4])  # 像表格中写入数据（对应的行和列）
            k=k+1
            workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


if __name__ == '__main__':
    main()
    input("执行完成................!")
