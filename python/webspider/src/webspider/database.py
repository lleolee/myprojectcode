'''
Created on 2017��4��24��

@author: lleo
'''
# -*- coding: utf-8 -*-
class database(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def savefile(self,path,data):
        f_obj = open(path,'wb')
        f_obj.write(bytes(data.encode('utf-8')))
        f_obj.close()    