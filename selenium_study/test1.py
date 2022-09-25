from selenium import webdriver
from lxml import etree
import time
import re
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://world.huanqiu.com/article/49ndtuUUjus'
# 打开
browser.get(url)
time.sleep(1)

content = browser.page_source
tree = etree.HTML(content)

text_list = tree.xpath('//div[@class="content"]//p/text()')
print(len(text_list))
