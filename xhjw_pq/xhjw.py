from selenium import webdriver
from lxml import etree
import time
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
list_num = 0
next_button = browser.find_elements_by_xpath('//li[@id="dataMoreBtn"]')[0]
for i in range(3):
    next_button.click()
    button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')
    print(len(button_list))
    time.sleep(3)
print('-----------------')
button_list = browser.find_elements_by_xpath('//ul[@id="showData0"]/li/h3/a')
# button_list = button_list[list_num:]
content = browser.page_source  # 获取网页源码
tree = etree.HTML(content)
title = tree.xpath('//ul[@id="showData0"]/li/h3/a/text()')
list_img = tree.xpath('//ul[@id="showData0"]//i[@class="imgs"]//img/@data-original')
for img in list_img:
	with open('./pic/' + '图片.txt', 'a', encoding='utf-8')as fp:
		fp.write(img)
		fp.write('\n')
for button in button_list:
	print(title[title_cont])
	button.click()
	handles = browser.window_handles
	browser.switch_to.window(handles[-1])  # 将标识符移到新的页面
	time.sleep(1)
	info_content = browser.page_source  # 获取新页面网页源码
	tree1 = etree.HTML(info_content)
	text_list = tree1.xpath('//div[@id="detail"]//p/text()')
	print(len(text_list))
	for text in text_list:
		text = text.replace(u'\xa0', '')
		with open('./info/' + title[title_cont] + '.text', 'a', encoding='utf-8') as fp:
			fp.write(text)
			fp.write('\n')
	img_list = tree1.xpath('//div[@id="detail"]/p/img/@src')
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
		with open('./pic/' + '图片' + '.txt', 'a', encoding='utf-8') as fp:
			fp.write(img_src)
			fp.write('\n')
	browser.close()  # 关闭当前页面
	time.sleep(2)
	browser.switch_to.window(handles[0])  # 将标识符移到首页
	title_cont = title_cont + 1
