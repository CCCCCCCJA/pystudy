from selenium import webdriver
from lxml import etree
import time
import urllib.request
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url
url = 'https://mil.ifeng.com/shanklist/originalcard/14-35082-'
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
src_list = tree.xpath('//ul[@class="clearfix-1DdjgYVR"]/li/a/@href')
# 首页获取的标题名称
title = tree.xpath('//ul[@class="clearfix-1DdjgYVR"]/li/a/@title')
# 首页标题中的图片地址
list_pic = tree.xpath('//ul[@class="clearfix-1DdjgYVR"]/li/a/p/img/@src')
print(len(title))
print(len(src_list))
print(len(list_pic))
for img in list_pic:
    with open('./pic1/' + '图片.txt', 'a', encoding='utf-8')as fp:
        fp.write(img)
        fp.write('\n')
title_count = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
for src in src_list:
    browser.get(src)
    time.sleep(2)
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])  # 将标识符移到新的页面
    info_content = browser.page_source  # 获取新页面网页源码
    tree1 = etree.HTML(info_content)
    info_list = tree1.xpath('//div[@class="main_content-r5RGqegj"]/div/div')
    info = []
    img_list = []
    video_list = []
    time_info = tree1.xpath('//div[@class="timeBref-2lHnksft"]//a/text()')
    info.append(title[title_count])
    if len(time_info) > 0:
        info.append(time_info[0])
    for i in info_list:
        p = i.xpath('.//p/text()')
        img = i.xpath('.//p/img/@data-lazyload')
        video = i.xpath('.//video/@src')
        # print(len(video))
        if len(p) != 0:
            for k in p:
                infos = k.replace(u'\xa0', '')
                info.append(infos)
        if len(img) != 0:
            for k in img:
                # infos = k.replace(u'\xa0', '')
                info.append("[image: " + k + "]")
                img_list.append(k)
        if len(video) != 0:
            for k in video:
                info.append("[video: " + k + "]")
                video_list.append(k)
    # print(info)
    print(title[title_count])
    title_count += 1
    time.sleep(1)
    try:
        info.remove('[APP专享]野外发现红包袱 打开一看众人惊呆')
        info.remove('下载客户端观看')
        info.remove('This is a modal window.')
        info.remove('Beginning of dialog window. Escape will cancel and close the window.')
        info.remove('End of dialog window.')
    except:
        print('移除出错！')
    try:
        for k in info:
            title[title_count] = title[title_count].replace('/', ' ')
            # k = k.replace(u'\xa0', '')
            with open('./info1/' + title[title_count] + '.text', 'a', encoding='utf-8') as fp:
                fp.write('    '+k)
                fp.write('\n')
        for img in img_list:
            with open('./pic1/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
                fp.write(img)
                fp.write('\n')
        for vd in video_list:
            with open('./video1/' + '视频' + '.txt', 'a', encoding='utf-8') as fp:
                fp.write(vd)
                fp.write('\n')
    except:
        print('保存出错！')
    browser.back()  # 关闭当前页面
    time.sleep(2)
    browser.switch_to.window(handles[0])  # 将标识符移到首页
