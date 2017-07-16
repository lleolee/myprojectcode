#!/usr/bin/python3
# Filename: web.py
'''
Created on 2017年5月4日

@author: lleo
'''
import gzip

def ungzip(data):
    try:
        data = gzip.decompress(data)
        print('gzip decompressed ok...')
    except Exception as e:
        print(e)
        print('gzip decompressed err...')
    return data
        

class Utils(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        