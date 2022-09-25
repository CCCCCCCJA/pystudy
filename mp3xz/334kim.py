from selenium import webdriver
from lxml import etree
import time
import urllib.request
from urllib.request import quote
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'http://334.kim'
# 打开
browser.get(url)
time.sleep(1)
content = browser.page_source

tree = etree.HTML(content)

mp3_list = tree.xpath('//ul[@class="accordion"]/li/ul/li/a[@class="url"]/@hrefsrc')
name_list = tree.xpath('//ul[@class="accordion"]/li/ul/li/a[@class="url"]/text()')
i = 0
while(i != len(mp3_list)-1):
	src1 = mp3_list[i].split('//')[0] + '//' + mp3_list[i].split('//')[1]
	src2 = mp3_list[i].split('//')[2]
	mp3_src = src1 + '//' + quote(src2)
	urllib.request.urlretrieve(url=mp3_src, filename='./MP3/' + name_list[i])
	i = i + 1
	print('第' + str(i) + '个' + '下载成功')