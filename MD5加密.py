#md5进行数据的加密.。
import hashlib
#md5加密
def encryption_md5(name):
    m = hashlib.md5()  #创建一个hashlib.md5()对象
    m.update(name.encode("utf8"))    #将参数转换为UTF8编码
    print(m.hexdigest())            #用十六进制输出加密后的数据

encryption_md5("lucy")
encryption_md5("hello world")
encryption_md5("luboyan")
