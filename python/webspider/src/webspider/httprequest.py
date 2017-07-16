# -*- coding: utf-8 -*-
'''
Created on 2017Äê4ÔÂ24ÈÕ

@author: lleo
'''

#!/usr/bin/python3
# Filename: httprequest.py

import urllib.request
import http.cookiejar

class httprequest(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    def makeopener(self, head={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        header = []
        for key, value in head.items():
            elem = (key, value)
        opener.addheaders = header
        return opener
