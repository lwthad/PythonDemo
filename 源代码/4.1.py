# 根据网址爬取图片
import requests
import re
from bs4 import BeautifulSoup
def get_html(urllist):
    attrs = {}
    res = requests.get(urllist)
    soup = BeautifulSoup(res.text, 'html.parser')
    src = soup.find_all("img",attrs={"max-width":"600"},src=re.compile("http://")) #利用正则排除不全的网址
    return src

def down_img(url):
    i = 1
    for link in url:
        pic_url = link.get('src')  #图片url http://img.mp.itc.cn/upload/20170630/0eaf2b85b56b4cb18fcbe26ff03406f5_th.jpg
        pic = requests.get(pic_url).content
        #f = open("所爬图片\\%s.jpg"%pic_url[-14:-7],"wb")
        f = open("所爬图片\\%s.jpg"%i,"wb") #以数字命名便于后面处理
        i+=1
        f.write(pic)
        f.close()

url = get_html("http://www.sohu.com/a/153395967_118263")
down_img(url)
