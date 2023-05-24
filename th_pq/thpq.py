from selenium import webdriver
from lxml import etree
import time
import urllib.request
import os
# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Cookie': 'td_cookie=58969364; __bid_n=187e5916548de849074207; FPTOKEN=HKI+fI88lrTaSd2ZIowteySS+3kjmzr/BIFQ5jdT+aJRWKVWUq60Hh74rFdTBppaL9F9e3+iTGP8fNdxVPCknm0QIw+Funlxq0x5px28V1DCIapEHE0lL0h4/qyiT1AG20F5165wFxHsMjV/arsZKr/rSgMavT5r6YGA20+Tvka015rVIf3M+BG0ydo3yiYKtsh0SPuG6hCE5YKsY0Ze91AiGXJPj0ANrIlf01s0pCK54LoPaZyXEJhQuyhcQbCQkqt/UtuuHxIvBeLQzdpqcHOnnbzRE7n7nTHJ2MHupNMJR3SJZ6wJnv+6Y/vFw6dR8buISVlMK0m+zHtn4RLwkjbnzaoYSht6KlmSlXdRtvLjy912SrMhaM21huuUpxR3qt89OozZb8XHgONwHmNSqw==|ULILclCY9GG6xfu4smcUiH8dRZEQrZnwPCNly4wxgW8=|10|c150c5bcc180889bdf7dcca636dcfbce'
}
startpage = 1
endpage = 5
url = "http://app.taihainet.com/?app=system&controller=roll#channel=3024&size=50&page=2200"
browser.get(url)
time.sleep(3)
imgstr = []
# nextbutton = browser.find_elements_by_xpath('//a[@class="next"]')[0]
for page in range(1, endpage+1):
    errnum = 0
    if page != endpage:
        nextbutton = browser.find_elements_by_xpath('//a[@class="next"]')[0]
    content = browser.page_source  # 获取网页源码
    tree = etree.HTML(content)
    titlelist = tree.xpath('//ul[@id="data-container"]//li[@class="item"]/a[@class="title"]/text()')
    # titlelist = tree.xpath('//div[@class="A_L_con"]//p/a/text()')
    srclist = tree.xpath('//ul[@id="data-container"]//li[@class="item"]/a[@class="title"]/@href')
    # srclist = tree.xpath('//div[@class="A_L_con"]//p/a/@href')
    # print(len(titlelist), len(srclist))
    for i in range(len(srclist)):
        titlelist[i] = titlelist[i].replace(' ', '').replace('/', '').replace('、', '').replace(':', '').replace('.','').replace('|', '').replace('-', '').replace('?', '').replace(',', '')
        if os.path.exists('./info/' + titlelist[i] + '.txt'):
            print('跳过')
            continue
        try:
            request = urllib.request.Request(url=srclist[i], headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            newtree = etree.HTML(content)
            plist = newtree.xpath('//div[@class="article-content"]/p')
            # article-content
            # article-content fontSizeSmall BSHARE_POP
            info = []
            info.append(titlelist[i])
            timestr = newtree.xpath('//time/text()')[0]
            # timestr = newtree.xpath('//span[@id="pubtime_baidu"]/text()')[0]
            info.append(timestr)
            lylist = newtree.xpath('//span[@class="important-link"]//text()')
            # lytext1 = newtree.xpath('//span[@class="source_baidu"]/text()')[0]
            # lytext1 = lytext1.replace('\t', '').replace('\n', '')
            # lytext = '来源：' + lytext1
            lytext = ''
            for ly in lylist:
                res = ly.replace('\n', '').replace('\t', '')
                lytext += res
            info.append(lytext)
            video = newtree.xpath('//div[@class="article-container"]//script[@class="cmstopVideo"]/@src')
            if len(video) != 0:
                for vs in video:
                    info.append('[video:' + vs + ']')
            for pp in plist:
                img = pp.xpath('.//img/@src')
                if len(img) != 0:
                    for imgsrc in img:
                        info.append('[image:' + imgsrc + ']')
                    with open("imgsrc.txt", 'a', encoding='utf-8') as fp:
                        for imgs in img:
                            fp.write(imgs + '\n')
                text = pp.xpath('.//text()')
                if len(text) != 0:
                    for tt in text:
                        rtt = tt.replace(' ', '').replace('\n', '').replace('\t', '').replace('\u3000', '')
                        info.append(rtt)
        except Exception:
            print('标题时间等错误！！！')
            errnum += 1
            continue
        titlelist[i] = titlelist[i].replace(' ', '').replace('/', '').replace('、', '').replace(':', '').replace('.','').replace('|', '').replace('-', '').replace('?', '').replace(',', '').replace('"', '')
        try:
            if len(plist) > 0:
                with open('./info/' + titlelist[i] + '.txt', 'a', encoding='utf-8') as fp:
                    tag = 0
                    for tt in info:
                        fp.write('    ' + tt)
                        fp.write('\n')
                fp.close()
                print(titlelist[i])
            else:
                tlist = newtree.xpath('//div[@class="article-content"]//text()')
                for tt in tlist:
                    rtt = tt.replace(' ', '').replace('\n', '').replace('\t', '').replace('\u3000', '')
                    info.append(rtt)
                if len(tlist) > 0:
                    with open('./info/' + titlelist[i] + '.txt', 'a', encoding='utf-8') as fp:
                        for tt in info:
                            if len(tt) > 2:
                                fp.write('    ' + tt)
                                fp.write('\n')
                            else:
                                fp.write(tt)
                    fp.close()
                    print(titlelist[i])
                else:
                    print('xpath错误！！！！！！')
                    errnum += 1
        except Exception:
            print('保存错误！！！', titlelist[i])
            errnum += 1
            continue
    if errnum > 25:
        break
    print('第' + str(page) + '页已保存完成' + 'errnum : ' + str(errnum))
    print('--------------------------------------')
    nextbutton.click()
    time.sleep(4)