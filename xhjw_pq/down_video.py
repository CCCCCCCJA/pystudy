import urllib.request
with open('./pic/视频.txt', 'r')as fp:
	for url in fp:
		# url = 'http:' + url
		url_info = url[-25:].replace('\n', '')
		url_info = url_info.replace('/', '')
		url_info = url_info.replace('.f30', '')
		print(url_info)
		urllib.request.urlretrieve(url, './video/'+url_info)
		print('下载成功！')