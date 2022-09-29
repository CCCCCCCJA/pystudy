import urllib.request
with open('./pic/图片1.txt', 'r')as fp:
	for url in fp:
		url = 'http:' + url
		url_info = url[-25:].replace('\n', '')
		url_info = url_info.replace('?w=1260', '')
		# print(url_info)
		urllib.request.urlretrieve(url, './img/'+url_info)
		print('下载成功！')