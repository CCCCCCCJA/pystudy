from selenium import webdriver
from lxml import etree
import time
import urllib.request
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.sohu.com/xtopic/TURBd01EVTBPREl5?spm=smpc.channel_218.block4_113_ig4zpQ_1_link.1.1676874363788iNzqRLH_499'
# 打开
browser.get(url)
time.sleep(1)
xwlist = browser.find_elements_by_xpath('//div[@class="FeedList"]/div/a[@class="tpl-image-text-feed-item-content"]')
for xw in xwlist:
    xw.click()
    time.sleep(1)
    handles = browser.window_handles
    browser.switch_to.window(handles[-1])  # 将标识符移到新的页面
    content = browser.page_source  # 获取网页源码
    tree = etree.HTML(content)
    # print(content)
    info = []
    try:
        elementlist = tree.xpath('//article[@id="mp-editor"]/*')
        for el in elementlist:
            img = el.xpath('.//img/@src')
            text = el.xpath('.//text()')
            if len(img) != 0:
                for imgsrc in img:
                    info.append('[image:' + imgsrc + ']')
            else:
                for tt in text:
                    info.append(tt)
        info[0] = info[0].replace('原标题：', '')
        timeinfo = '时间：' + tree.xpath('//span[@id="news-time"]/text()')[0]
        info.insert(1, timeinfo)
        lyinfo = '来源：' + tree.xpath('//div[@class="user-info"]/h4/a/text()')[0]
        info.insert(1, lyinfo)
    except Exception:
        print('xpath错误！！！')
    try:
        with open('./info/' + info[0] + '.txt', 'w', encoding='utf-8') as fp:
            for infoinfo in info:
                fp.write('    ' + infoinfo + '\n')
            print(info[0])
    except Exception:
        print('文件保存错误！！！')
    browser.close()  # 关闭当前页面
    time.sleep(1)
    browser.switch_to.window(handles[0])