from selenium import webdriver
from lxml import etree
import time
import re
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'http://www.xinhuanet.com/mil/shijie.htm'
# 打开
browser.get(url)
time.sleep(1)

title_cont = 0
next_button = browser.find_elements_by_xpath('//li[@id="dataMoreBtn"]')[0]
for i in range(10):
    next_button.click()
    button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')
    print(len(button_list))
    time.sleep(3)
print('-----------------')
# print(len(button_list))


content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
title = tree.xpath('//ul[@id="showData0"]/li/h3/a/text()')
print(title[title_cont])
for button in button_list:
    # list_num = int(list_num + 1)
    button.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])  # 将标识符移到新的页面
    info_content = browser.page_source  # 获取新页面网页源码
    tree = etree.HTML(info_content)
    text_list = tree.xpath('//div[@id="detail"]//p/text()')
    if not text_list:
        text_list = tree.xpath('//div[@id="p-detail"]//p/text()')
        for text in text_list:
            text = text.replace(u'\xa0', '')
            with open('./info/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
                fp.write(text)
                fp.write('\n')
        img_list = tree.xpath('//div[@id="p-detail"]//p//img/@src')
        if (len(img_list) > 1):
            for img in img_list:
                src = ''
                current_url = browser.current_url
                s = current_url.split('/')
                for i in range(len(s) - 1):
                    if (i != len(s) - 1):
                        src = src + s[i] + '/'
                    else:
                        src = src + s[i]
                img_src = src + img
                with open('./pic/' + '图片' + '.text', 'a', encoding='utf-8') as fp:
                    fp.write(img_src)
                    fp.write('\n')
    else:
        for text in text_list:
            text = text.replace(u'\xa0', '')
            with open('./info/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
                fp.write(text)
                fp.write('\n')
        img_list = tree.xpath('//div[@id="detail"]//img/@src')
        if (len(img_list) > 1):
            for img in img_list:
                src = ''
                current_url = browser.current_url
                s = current_url.split('/')
                for i in range(len(s) - 1):
                    if (i != len(s) - 1):
                        src = src + s[i] + '/'
                    else:
                        src = src + s[i]
                img_src = src + img
                with open('./pic/' + '图片' + '.text', 'a', encoding='utf-8') as fp:
                    fp.write(img_src)
                    fp.write('\n')
    # time.sleep(1)
    browser.close()  # 关闭当前页面
    time.sleep(2)
    browser.switch_to.window(handles[0])  # 将标识符移到首页
    title_cont = title_cont + 1