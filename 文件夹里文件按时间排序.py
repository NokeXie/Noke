import os

result_dir = r'\\192.168.10.212\FileSystem\Data\ow_tro\fmd\pdf'

lists = os.listdir(result_dir)  # 获得文件夹内所有文件

lists.sort(key=lambda fn: os.path.getmtime(result_dir + '\\' + fn))  # 排序

print('new file is : ' + lists[-1])  # 最新的文件名

file = os.path.join(result_dir, lists[-1])  # 把文件路径和文件名链接到一起

print('file path is : ' + file)