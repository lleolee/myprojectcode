#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 20170424
@author: lleo
'''

import re
import collections
import http.cookiejar
from webspider.httprequest import httprequest
from webspider.database import database


class webspider(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        queue = collections.deque()
        visited = set()
        
        url = 'http://www.baidu.com'
        queue.append(url)
        cnt = 0
        
        while queue:
            url = queue.popleft()
            visited.add(url)
            
            print('catching:'+str(cnt)+':url='+url)
            cnt +=1
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
                oper = httprequest.makeopener()
                uop = oper.open(url,timeout=1000)
            except:
                print('urlopen failed ' + str(cnt)+'...')
                continue
            '''if 'html' not in urlop.getheader('Content-Type'):'''
            if 'html' not in uop.getheader('Content-Type'):
                continue
        
            try:
                #data = urlop.read().decode('utf-8')
                data = uop.read().decode('utf-8')
            except:
                continue
            finally:
                if cnt > 16 : 
                    break
        linkre = re.compile('href=\"(.+?)\"')
        for x in linkre.findall(data):
            if 'http' in x and x not in visited:
                queue.append(x)
                print('add queue:'+str(len(queue))+':'+x)
        database.savefile('D:\\tmp\\'+url[8:16]+'.html',data)