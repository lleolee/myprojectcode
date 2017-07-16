# -*- coding: utf-8 -*-
#!/usr/bin/python3
# Filename: web.py
'''
Created on 2017年4月25日

@author: lleo
'''
def savefile(path, data):
    f_obj = open(path, 'wb')
    f_obj.write(bytes(data.encode('utf-8')))
    f_obj.close()    

class Database(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
