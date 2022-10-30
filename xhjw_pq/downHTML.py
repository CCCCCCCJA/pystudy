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
url = 'http://www.mil.xinhuanet.com/guandian.htm'
# 打开
browser.get(url)
time.sleep(1)
title_cont = 0
list_num = 0
next_button = browser.find_elements_by_xpath('//li[@id="dataMoreBtn"]')[0]
try:
    for i in range(10):
        # 点击按钮
        next_button.click()
        # button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')
        # print(len(button_list))
        print(i)
        time.sleep(4)
except:
    print('++++++++++++++++++++')

time.sleep(2)
content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
# 每个新闻详情页的地址
src_list = tree.xpath('//ul[@id="showData0"]/li/h3/a/@href')
# 首页获取的标题名称
title = tree.xpath('//ul[@id="showData0"]/li/h3/a/text()')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
for src in src_list:
    # request = urllib.request.Request(url=src, headers=headers)
    # response = urllib.request.urlopen(request)
    # content = response.read().decode('utf-8')
    try:
        urllib.request.urlretrieve(src, './html/' + title[title_cont] + '.html')
    except:
        print("----")
    title_cont += 1
    print(title[title_cont])

