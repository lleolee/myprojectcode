# -*- coding: utf-8 -*-
#!/usr/bin/python3
# Filename: web.py
'''
Created on 2017年4月25日

@author: lleo
'''
import re
import collections
import bs4
import urllib.parse
# from lycrawler 
import web, database, utils
from pip._vendor.requests.exceptions import HTTPError

def test():
    url = 'http://www.zhihu.com/'
    opener = web.get_opener()
    op = opener.open(url)
    data = op.read()
    print(data.decode('utf-8'))
#     data = utils.ungzip(data)
    _xsrf = web.getXSRF(data.decode())
    
    print(_xsrf)
    
    url += 'login'
    id = '18108284725'
    password = '860501'
    postDict = {
            '_xsrf':_xsrf,
            'email': id,
            'password': password,
            'rememberme': 'y'
    }
    postData = urllib.parse.urlencode(postDict).encode()
    print(url)
    print(postData.decode('utf-8'))
    
    try:
        opener = web.get_opener()
        op = opener.open(url, postData)
    except HTTPError as e:
        print(e)
        print('err')
    print('eeee')    
    data = op.read()
    print(data.decode('utf-8'))
    print('finish...')
#     data = utils.ungzip(data) 
    
    print(data.decode())  

def main():
    queue = collections.deque()
    visited = set()
    
    url = 'http://www.baidu.com'
    queue.append(url)
    cnt = 0
    
    while queue:
        url = queue.popleft()
        visited.add(url)
        
        print('catching:' + str(cnt) + ':url=' + url)
        cnt += 1
        try:
            '''
            httpreq = urllib.request.Request(url,headers = {
                'Connection': 'Keep-Alive',
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                'User-Agent': 'Mozilla/6.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
            })
            urlop = urllib.request.urlopen(httpreq,timeout=3)
            '''
            oper = web.get_opener();
            url_open = oper.open(url,timeout=10)
        except HTTPError as e:
            print('urlopen failed ' + str(cnt) + '...' + e)
            continue
        
        if url_open is None:
            print('url is not found')
            continue
        
        '''if 'html' not in urlop.getheader('Content-Type'):'''
        if 'html' not in url_open.getheader('Content-Type'):
            continue
    
        try:
            # data = urlop.read().decode('utf-8')
            data = url_open.read().decode('utf-8')
        except:
            continue
        finally:
            if cnt > 16 : 
                break
        bsObj = bs4.BeautifulSoup(data, 'html.parser')
        
        linkre = re.compile('href=\"(.+?)\"')
        for x in linkre.findall(data):
            if 'http' in x and x not in visited:
                queue.append(x)
                print('add queue:' + str(len(queue)) + ':' + x)
        database.savefile('D:\\tmp\\' + url[8:16] + '.html', data)
    
    
__name__ = '__main__'    
if __name__ == '__main__':
#     print('start main...')
#     main()
    print('start test...')
    test()
