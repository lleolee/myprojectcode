#!/usr/bin/env python
import io
import formatter
import html.parser
import http.client
import urllib
import os
from urllib.parse import urlparse

class Retriever(object):
    __slots__ = ('url','file')
    def __init__(self,url):
        self.url,self.file = self.get_file(url)
    
    def get_file(self,url,default='index.html'):
        'Create usable local filename from URL'
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        filepath = '%s%S' % (host,parsed.path)[1]
        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath,default)
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url,filepath
    
    def download(self):
        'Download URL to specific named file'
        try:
            retval = urllib.request.urlretrieve(self.url,self.file)
        except(IOError) as e:
            retval = (('***ERROR: bad URL "%s":%s'%(self.url,e)),)
        return retval
    
    def parse_links(self):
        'Parse out the links found in download HTML file'
        f = open(self.file,'r')
        data = f.read()
        f.close()
        parser = html.parser.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(io.StringIO())))
        parser.feed(data)
        parser.close
        return parser.anchorlist

class Crawler(object):
    count = 0
    
    def __init__(self,url):
        self.q = [url]
        self.seen = set()
        parsed  = urllib.parse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])
        
        
    
        