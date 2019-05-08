from urllib.request import urlopen
from bs4 import BeautifulSoup
def tianqi():
    resp=urlopen('http://www.weather.com.cn/weather/101190302.shtml')
    soup=BeautifulSoup(resp,'html.parser')
    tagDate=soup.find('ul', class_="t clearfix")
    dates=tagDate.h1.string

    tagToday=soup.find('p', class_="tem")
    try:
        temperatureHigh=tagToday.span.string
    except AttributeError as e:
        temperatureHigh=tagToday.find_next('p', class_="tem").span.string

    temperatureLow=tagToday.i.string
    weather=soup.find('p', class_="wea").string

    tagWind=soup.find('p',class_="win")
    winL=tagWind.i.string

    return ('今天是：'+dates +"\n"
            '风级：'+winL +"\n"
            '最低温度：'+temperatureLow +"\n"
            '最高温度：'+temperatureHigh +"\n"
            '天气：'+weather)
if __name__ == '__main__':
    print(tianqi())