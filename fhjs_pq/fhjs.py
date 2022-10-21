from selenium import webdriver
from lxml import etree
import time
import urllib.request
import re

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
# url

url = 'https://mil.ifeng.com/shanklist/14-35083-'
# 打开
browser.get(url)
time.sleep(1)
title_cont = 0
# 已经爬取的数量
list_num = 0
# 获取显示更多的按钮
# next_button = browser.find_elements_by_xpath('//a[@class="news-stream-basic-more"]')[0]
try:
	for i in range(50):
		next_button = browser.find_elements_by_xpath('//a[@class="news-stream-basic-more"]')[0]
		# 点击按钮
		next_button.click()
		time.sleep(4)
except IndexError as e:
	print(e)

print('-----------------')
time.sleep(2)
content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
# 每个新闻详情页的地址
src_list = tree.xpath('//div[@class="news-stream-newsStream-news-item-infor"]/h2/a/@href')
# 首页获取的标题名称
title = tree.xpath('//div[@class="news-stream-newsStream-news-item-infor"]/h2/a/@title')
# 首页标题中的图片地址
list_pic = tree.xpath('//ul[@class="news-stream-basic-news-list"]/li/a/img/@src')
# print(len(src_list), len(title), len(list_pic))
# 对获取的列表进行分割   取出已经获取 的内容
list_pic = list_pic[list_num:]
src_list = src_list[list_num:]
title = title[list_num:]
print(f'总数：{len(title)}')
print('-----------------')
# print(len(src_list), len(title), len(list_pic))
# 保存标题首页标题中的图片
for img in list_pic:
	with open('./tit_pic1/' + '图片.txt', 'a', encoding='utf-8')as fp:
		fp.write('https:' + img)
		fp.write('\n')
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
for src in src_list:
	# 使用urllib获取网页资源
	src = 'https:' + src
	request = urllib.request.Request(url=src, headers=headers)
	response = urllib.request.urlopen(request)
	content = response.read().decode('utf-8')
	tree = etree.HTML(content)
	# 获取详情页中的text
	text_list = tree.xpath('//div[@class="text-3w2e3DBc"]/p/text()')
	time = tree.xpath('//div[@class="timeBref-2lHnksft"]/a/text()')
	title[title_cont] = title[title_cont].replace('/', '')
	with open('./info1/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
		fp.write(time[0])
		fp.write('\n')
	for text in text_list:
		# 将标题中的'/'去除   防止在保存文件的时候发生异常
		title[title_cont] = title[title_cont].replace('/', '')
		text = text.replace(u'\xa0', '')
		with open('./info1/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
			fp.write(text)
			fp.write('\n')
	# 获取详情页中的图片地址
	img_list = tree.xpath('//div[@class="text-3w2e3DBc"]/p/img/@data-lazyload')
	for img in img_list:
		with open('./tit_pic1/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
			fp.write(img)
			fp.write('\n')
	print(title[title_cont])
	title_cont = title_cont + 1
