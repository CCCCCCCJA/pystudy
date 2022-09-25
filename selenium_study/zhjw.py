from selenium import webdriver
from lxml import etree
import time
import re
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://military.china.com/news/'
# 打开
browser.get(url)
time.sleep(1)
title_cont = 0
content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
title = tree.xpath('//ul[@class="item_list"]/li/h3/a/text()')
# img_src = tree.xpath('//ul[@class="item_list"]/li/a/img/@data-original')

button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')