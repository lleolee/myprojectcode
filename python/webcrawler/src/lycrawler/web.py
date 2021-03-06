# -*- coding: utf-8 -*-
#!/usr/bin/python3
# Filename: web.py
'''
Created on 2017年4月25日

@author: lleo
'''
import http.cookiejar
import urllib.request
import re

def get_opener(head={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }):
    cookie_jar = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(handler)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"')
    strlist = cer.findall(data)
    return strlist[0]

class Web(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
