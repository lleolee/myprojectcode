'''
Created on 2017年5月29日

@author: lleo
'''
class ResultDoubleColor:

    def __init__(self, double_color = []):
        self.__result_double_color = double_color
        
    def __str__(self):
        str_ret = ''
        for elem in self.__result_double_color:
            if elem:
                str_ret+=(str(elem))
        return str_ret


    def get_result_double_color(self):
        return self.__result_double_color

    def set_result_double_color(self, id, value):
        for elem in self.__result_double_color:
            if id is elem.get_id():
                elem.set_red()
                elem.set_blue()
                
    def add_result_double_color(self, value):
        self.__result_double_color.append(value)

    def del_result_double_color(self):
        for elem in self.__result_double_color:
            elem.del_id()
            elem.del_red()
            elem.del_blue()

    result_double_color = property(get_result_double_color, set_result_double_color, del_result_double_color, "result_double_color's docstring")



class DoubleColor(object):
    '''
    classdocs
    '''
    def __init__(self, id=None, red=None, blue=None):
        '''
        Constructor
        '''
        self.__id = id
        self.__red = red
        self.__blue = blue

    def __str__(self):
        str_ret = str(self.__id) + ' '
        for i,value in enumerate(self.__red):
            str_ret += (value + ' ')
        
        return str_ret + ' '+str(self.__blue) + '\n'


    def get_id(self):
        return self.__id


    def get_red(self):
        return self.__red


    def get_blue(self):
        return self.__blue


    def set_id(self, value):
        self.__id = value


    def set_red(self, value):
        self.__red = value


    def set_blue(self, value):
        self.__blue = value


    def del_id(self):
        self.__id = ''


    def del_red(self):
        del self.__red


    def del_blue(self):
        self.__blue = ''

    id = property(get_id, set_id, del_id, "id's docstring")
    red = property(get_red, set_red, del_red, "red's docstring")
    blue = property(get_blue, set_blue, del_blue, "blue's docstring")



        
