import os
import xlwt
import sys
import types
def write_excel():
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')

    # 列表格式数据
    excelData = "dsadasd"
    # 定义循环下标

    data_sheet.write(0,0,excelData)
    # sys.exit();
    # 保存文件
    workbook.save('D:\demo.xls')

if __name__ == '__main__':
    write_excel()
print('创建demo.xlsx文件成功')