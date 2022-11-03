from selenium import webdriver
from lxml import etree
import time
import urllib.request
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://ishare.ifeng.com/mediaShare/home/1604031/media'
# 打开
browser.get(url)
time.sleep(2)
js_button ='document.documentElement.scrollTop=100000'
for i in range(10):
    browser.execute_script(js_button)
    time.sleep(2)
# 获取网页源码
content = browser.page_source
# 进行xpath解析
tree = etree.HTML(content)
# 每个新闻详情页的地址
src_list = tree.xpath('//a[@class="index_title_WzMk9"]/@href')
# 首页获取的标题名称
title = tree.xpath('//a[@class="index_title_WzMk9"]/text()')
# 首页标题中的图片地址
# list_pic = tree.xpath('//ul[@class="clearfix-1DdjgYVR"]/li/a/p/img/@src')
print(len(title))
print(len(src_list))
# print(len(list_pic))
# for img in list_pic:
#     with open('./jijin/pic2/' + '图片.txt', 'a', encoding='utf-8')as fp:
#         fp.write(img)
#         fp.write('\n')
title_count = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
for tmp in src_list:
    src = "http:" + tmp
    request = urllib.request.Request(url=src, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree1 = etree.HTML(content)