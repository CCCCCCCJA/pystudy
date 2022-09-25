
# https://movie.douban.com/j/chart/top_list?type=5
# &interval_id=100%3A90&action=&start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=5
# &interval_id=100%3A90&action=&start=20&limit=20

import urllib.request
import urllib.parse
def create_request(page):
    base_url='https://world.huanqiu.com/api/list?node=%22/e3pmh22ph/e3pmh2398%22,%22/e3pmh22ph/e3pmh26vv%22,%22/e3pmh22ph/e3pn6efsl%22,%22/e3pmh22ph/efp8fqe21%22&'
    data = {
        'offset':(page-1)*20,
        'limit':20
    }
    data = urllib.parse.urlencode(data)
    url = base_url+data
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf8')

    return content

def down_load(page, content):
    with open('./hqsb/douban'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)
    print('下载成功！！！')


# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page+1):
        # print(page)
        request = create_request(page) #每一页的请求对象
        content=get_content(request) # 获取响应数据
        down_load(page, content) # 下载