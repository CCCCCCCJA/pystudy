from selenium import webdriver
from lxml import etree
import time
import urllib.request
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://mil.ifeng.com/shanklist/14-35083-'
# 打开
browser.get(url)
next_button = browser.find_elements_by_xpath('//*[@id="root"]//a[@class="news-stream-basic-more"]')[0]
try:
    for i in range(10):
        next_button.click()
        time.sleep(3)
        next_button = browser.find_elements_by_xpath('//*[@id="root"]//a[@class="news-stream-basic-more"]')[0]
except:
    print('---------------------------')
# 获取网页源码
content = browser.page_source
# 进行xpath解析
tree = etree.HTML(content)
# 每个新闻详情页的地址    获取的连接没有https的头  在访问时需要加上
src_list = tree.xpath('//*[@id="root"]/div[5]/div[1]/div/ul/li/div/h2/a/@href')
# 首页获取的标题名称
title = tree.xpath('//*[@id="root"]/div[5]/div[1]/div/ul/li/div/h2/a/@title')
# 首页标题中的图片地址  获取的连接没有https的头  在保存时需要加上
list_pic = tree.xpath('//*[@id="root"]/div[5]/div[1]/div/ul/li/a/img/@src')
print(len(title))
print(len(src_list))
print(len(list_pic))
# 将标题中的图片保存到txt文件中
for img in list_pic:
    with open('./pic/' + '图片.txt', 'a', encoding='utf-8')as fp:
        img = 'http:' + img
        fp.write(img)
        fp.write('\n')
title_count = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
print(title[title_count])
for tmp in src_list:
    src = "http:" + tmp
    # 使用urllib获取网页资源
    request = urllib.request.Request(url=src, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree1 = etree.HTML(content)
    info_list = tree1.xpath('//div[@class="text-3w2e3DBc"]//p')
    info = []
    img_list = []
    time_info = tree1.xpath('//div[@class="timeBref-2lHnksft"]//a/text()')
    info.append(title[title_count])
    info.append(time_info[0])
    for i in info_list:
        c = i.xpath('./text()')
        if len(c) != 0:
            # print(c)
            for k in c:
                infos = k.replace(u'\xa0', '')
                info.append(infos)
        else:
            img = i.xpath('./img/@data-lazyload')
            strong = i.xpath('./strong/text()')
            if len(img) != 0:
                # src1 = ''
                # current_url = src
                # s = current_url.split('/')
                # for i in range(len(s) - 1):
                #     if (i != len(s) - 1):
                #         src1 = src1 + s[i] + '/'
                #     else:
                #         src1 = src1 + s[i]
                img_src = img[0]
                # print(img_src)
                info.append("[image: " + img_src + "]")
                img_list.append(img_src)
            if len(strong) != 0:
                # print(strong)
                for k in strong:
                    infos = k.replace(u'\xa0', '')
                    info.append(infos)
    try:
        for k in info:
            title[title_count] = title[title_count].replace('/', ' ')
            # k = k.replace(u'\xa0', '')
            with open('./info/' + title[title_count] + '.text', 'a', encoding='utf-8') as fp:
                fp.write('    '+k)
                fp.write('\n')
        for img in img_list:
            with open('./pic/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
                fp.write(img)
                fp.write('\n')
    except:
        print('-----')
    title_count += 1


