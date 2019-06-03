import xlrd
data = xlrd.open_workbook(r"\\192.168.10.56\天润文件\02-人力资源部\06-花名册\2019年TR花名册.xlsx")
table = data.sheets()[1]  # 获取天润值班排班表.xlsx 文件的表一
nrows = table.nrows  # 获取天润值班排班表.xlsx 文件的表一的有效行数
def renyuan():
    list=[]
    for i in range(nrows):   # 循环逐行打印
        if i == 0 or i == 1:  # 跳过第一和第二行
            continue
        k = table.row_values(i)[6:7] # 获取第i行的第二列数值(列表形式）例如['2019-4-1']
        list.append(k[0])
    return list
