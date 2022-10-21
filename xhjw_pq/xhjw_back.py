from selenium import webdriver
from lxml import etree
import time
import urllib.request
import re
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
# 世界   http://www.xinhuanet.com/mil/shijie.htm
# 中国   http://www.mil.xinhuanet.com/zhongguo.htm
# 观点   http://www.mil.xinhuanet.com/guandian.htm
# 军医   http://www.mil.xinhuanet.com/junyi.htm
url = 'http://www.mil.xinhuanet.com/junyi.htm'
# 打开
browser.get(url)
time.sleep(1)
title_cont = 0
# 已经爬取的数量
list_num = 0
# 获取显示更多的按钮
next_button = browser.find_elements_by_xpath('//li[@id="dataMoreBtn"]')[0]
for i in range(5):
    # 点击按钮
    next_button.click()
    # button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')
    # print(len(button_list))
    print(i)
    time.sleep(4)
print('-----------------')
time.sleep(2)
content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
# 每个新闻详情页的地址
src_list = tree.xpath('//ul[@id="showData0"]/li/h3/a/@href')
# 首页获取的标题名称
title = tree.xpath('//ul[@id="showData0"]/li/h3/a/text()')
# 首页标题中的图片地址
list_pic = tree.xpath('//ul[@id="showData0"]//i[@class="imgs"]//img/@data-original')
# print(len(src_list), len(title), len(list_pic))
# 对获取的列表进行分割   取出已经获取 的内容
list_pic = list_pic[list_num:]
src_list = src_list[list_num:]
title = title[list_num:]
# print(len(src_list), len(title), len(list_pic))
# 保存标题首页标题中的图片
for img in list_pic:
	with open('./pic1/' + '图片.txt', 'a', encoding='utf-8')as fp:
		fp.write(img)
		fp.write('\n')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

for src in src_list:
    # 使用urllib获取网页资源
    request = urllib.request.Request(url=src, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree = etree.HTML(content)
    # 获取详情页中的text
    text_list = tree.xpath('//div[@id="p-detail"]//p/text()')
    for text in text_list:
        # 将标题中的'/'去除   防止在保存文件的时候发生异常
        title[title_cont] = title[title_cont].replace('/', ' ')
        text = text.replace(u'\xa0', '')
        with open('./info1/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
            fp.write(text)
            fp.write('\n')
    # 获取详情页中的图片地址
    img_list = tree.xpath('//div[@id="p-detail"]/p//img/@src')
    for img in img_list:
        # 获取正确的图片src地址
        src1 = ''
        current_url = src
        s = current_url.split('/')
        for i in range(len(s) - 1):
            if (i != len(s) - 1):
                src1 = src1 + s[i] + '/'
            else:
                src1 = src1 + s[i]
        img_src = src1 + img
        # print(img_src)
        # 将图片地址写入文件中
        with open('./pic1/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
            fp.write(img_src)
            fp.write('\n')
    print(title[title_cont])
    title_cont = title_cont + 1
    