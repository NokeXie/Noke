import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')  #调用大漠插件
print(dm.ver())#输出版本号