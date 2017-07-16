#!/usr/bin/env python

import urllib.request,urllib.error,urllib.parse
from pip import req
from _overlapped import NULL

LOGIN="wesley"
PASSWD="you'll Never Guess"
URL="http://www.baidu.com"
REALM='Secure Archive'

def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,urllib.parse.urlparse(url)[1],LOGIN,PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib.request.Request(url)
    b64str = encodestring(bytes('%s:%s'%(LOGIN,PASSWD),'utf-8'))[:-1]
    req.add_header("Authorization", "Basic %s"%b64str)
    return req

for funcType in ('handler','request'):
    print('***Using %s:'% funcType.upper())
    url = eval('%s_version'% funcType)(URL)
    print('url:',url)
    f=urllib.request.urlopen(url)
    while not f.readline():
        print(str(f.readline(),'utf-8'))
    f.close()

