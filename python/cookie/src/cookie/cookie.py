'''
Created on 2017年5月17日

@author: lleo
'''
import urllib
import http.cookiejar

filename = 'cookie.txt'
#声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib.request.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('https://www.baidu.com/index.php?tn=request_10_pg')
if response is not None:
    page = response.read().decode()
    print('page:'+str(page))
    print(response)
if cookie is None:
    print('None')
else:
    print('not None')
    cookie.save();
for item in cookie:
    print( 'Name = '+item.name)
    print( 'Value = '+item.value)
    
class Cookie(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        