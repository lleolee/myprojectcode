'''
Created on 2017年5月17日

@author: lleo
'''
import urllib.request
import re



page = 1
url = 'http://www.qiushibaike.com/text/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

try:
    print(url)
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
#     print(content)
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

pattern = re.compile(r'<span>.*?</span>')
# print(content)
items = re.findall(pattern,content)
for item in items:
    hasimg = re.search('img', item)
    if not hasimg:
        print(item)


class Catchjoke(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        