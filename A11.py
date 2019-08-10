#coding=utf-8
from aip import AipOcr
import re
#百度文字识别
APPP_ID = '16734240'
API_KEY = 'IR7o3Aeig0398T8cVy26lKG2'
SECRET_KEY = 'BhwtR2smuoBNCDNM3oNeKTbRGXrrbGxP'
client = AipOcr(APPP_ID,API_KEY,SECRET_KEY)
i = open(r'D:\1111.png','rb')
img = i.read()
message = client.basicGeneral(img);
for i in message.get('words_result'):
    print(i.get('words'))

