from selenium import webdriver
from lxml import etree
import time
import urllib.request
import os
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Cookie': 'td_cookie=3100866743'
}
startpage = 1
endpage = 20
url = 'http://www.taihainet.com/news/twnews/bilateral/2023-03-01/2685208.html'
browser.get(url)
time.sleep(2)
content = browser.page_source
tree = etree.HTML(content)
print(content)
video = tree.xpath('//div[@class="article-container"]//script[@class="cmstopVideo"]/@src')
print(video)