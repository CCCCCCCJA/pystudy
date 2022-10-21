from selenium import webdriver
from lxml import etree
import time
import urllib.request
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
# 世界   http://www.xinhuanet.com/mil/shijie.htm
# 中国   http://www.mil.xinhuanet.com/zhongguo.htm
url = 'http://www.mil.xinhuanet.com/zhongguo.htm'
# 打开
browser.get(url)
time.sleep(1)
title_cont = 0
list_num = 236
next_button = browser.find_elements_by_xpath('//li[@id="dataMoreBtn"]')[0]
for i in range(35):
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
print(len(title))
# 获取时间
time_list = tree.xpath('//div[@class="info"]//span[@class="time"]/text()')
# 首页标题中的图片地址
list_pic = tree.xpath('//ul[@id="showData0"]//i[@class="imgs"]//img/@data-original')
# print(len(src_list), len(title), len(list_pic))
# 对获取的列表进行分割   取出已经获取 的内容
list_pic = list_pic[list_num:]
src_list = src_list[list_num:]
title = title[list_num:]
time_list = time_list[list_num:]
print(len(title))
print(len(src_list))
print(len(time_list))
for img in list_pic:
    with open('./pic1/' + '图片.txt', 'a', encoding='utf-8')as fp:
        fp.write(img)
        fp.write('\n')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
count = 0
for src in src_list:
    # 使用urllib获取网页资源
    request = urllib.request.Request(url=src, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree1 = etree.HTML(content)
    # 前20几个新闻详情页的div的id是detail
    info_list = tree1.xpath('//div[@id="p-detail"]//p')
    info = []
    img_list = []
    info.append(title[title_cont])
    info.append(time_list[title_cont])
    for i in info_list:
        c = i.xpath('./text()')
        if len(c) != 0:
            # print(c)
            for k in c:
                infos = k.replace(u'\xa0', '')
                info.append(infos)
        if len(c) == 0:
            img = i.xpath('./img/@src')
            font_img = i.xpath('./font/img/@src')
            strong = i.xpath('./strong/text()')
            p = i.xpath('./p/text()')
            font = i.xpath('./font/text()')
            if len(img) != 0:
                src1 = ''
                current_url = src
                s = current_url.split('/')
                for i in range(len(s) - 1):
                    if (i != len(s) - 1):
                        src1 = src1 + s[i] + '/'
                    else:
                        src1 = src1 + s[i]
                img_src = src1 + img[0]
                # print(img_src)
                info.append("[image: " + img_src + "]")
                img_list.append(img_src)
            if len(strong) != 0:
                # print(strong)
                for k in strong:
                    infos = k.replace(u'\xa0', '')
                    info.append(infos)
            if len(font_img) != 0:
                src1 = ''
                current_url = src
                s = current_url.split('/')
                for i in range(len(s) - 1):
                    if (i != len(s) - 1):
                        src1 = src1 + s[i] + '/'
                    else:
                        src1 = src1 + s[i]
                img_src = src1 + font_img[0]
                # print(img_src)
                info.append("[image: " + img_src + "]")
                img_list.append(img_src)
            if len(font) != 0:
                # print(font)
                for k in font:
                    infos = k.replace(u'\xa0', '')
                    info.append(infos)
            if len(p) != 0:
                # print(p)
                for k in p:
                    infos = k.replace(u'\xa0', '')
                    info.append(infos)
    try:
        for k in info:
            title[title_cont] = title[title_cont].replace('/', ' ')
            # k = k.replace(u'\xa0', '')
            with open('./info2/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
                fp.write('    '+k)
                fp.write('\n')
        for img in img_list:
            with open('./pic1/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
                fp.write(img)
                fp.write('\n')
    except:
        print('-----')
    count += 1
    print(title[title_cont])
    title_cont = title_cont + 1