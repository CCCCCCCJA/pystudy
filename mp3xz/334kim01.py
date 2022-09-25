from lxml import etree
import urllib.request
url = 'http://334.kim'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)
# 解析服务器响应文件
tree = etree.HTML(content)
# xpath的返回值是一个列表型的返回值
result = tree.xpath('//ul[@class="accordion"]/li/ul/li/a[@class="url"]/@hrefsrc')
print(result)

