'''
Created on 2017年6月2日

@author: lleo
'''
import urllib
import re
import bs4

import lottery.web 

def get_simulate_3d_all():
    result_d3d_all = []
    result_d3d_all=lottery.d3d.ResultD3d(result_d3d_all) 
    for i in range(1000):
        h = int(i/100)
        d = int(i/10%10)
        u = int(i%100%10)
        d3d_all=lottery.d3d.D3d(i,h,d,u,h+d+u,i)
        
        result_d3d_all.add_result_d3d(d3d_all)
    return result_d3d_all.get_result_d3d()

def get_lottery_3d():
    url='http://trend.caipiao.163.com/x3d/?beginPeriod=2008001&endPeriod=2017999'
#     url='http://trend.caipiao.163.com/x3d/?beginPeriod=2017001&endPeriod=2017999'
#     url='http://trend.caipiao.163.com/x3d/?beginPeriod=2008001&endPeriod=2017153'
#     url='http://trend.caipiao.163.com/x3d/?periodNumber=100'
    try:
        openner = lottery.web.get_opener()
        url_open = openner.open(url, data=None, timeout=10)
    except urllib.error.HTTPError as e:
        print('failed: open '+str(url).encode(encoding='utf_8', errors='strict'))
        print(e)
    finally:
        if url_open and 200 is url_open.getcode():
            print('url open OK')
        else:
            print('url: '+ str(url) +' is not found')
            return None

    try:
        data = url_open.read().decode('utf-8')
    except urllib.error as e:
        print('read data Err')
        print(e)
    finally:
        if data:
            print('read data OK')           
#             print('read data OK\n'+str(data))
        else:
            return None
    
    bs = bs4.BeautifulSoup(data, 'html.parser')
    result_d3d = []
    result_d3d=lottery.d3d.ResultD3d(result_d3d)
    for child_tr in bs.body.tbody.children:
        str_id = ''
        list_3d = []
        if child_tr:
            for child_td in child_tr:
#                 print(child_td)
                td_id = re.compile(r'<td>(.{7})</td>')
                id = td_id.findall(str(child_td))
                if id:
                    str_id = str(id[0])
#                     print('#####id######'+str(id))
                td_3d = re.compile(r'<td class="ball_[ro][er][da].*?js-fold".*?>(.*?)</td>')
                d3d_ball = td_3d.findall(str(child_td))
                if d3d_ball:
                    list_3d.append(int(d3d_ball[0]))
#                     print('#####red######'+str(red_ball))
               
        if list_3d:
#             print(str_id + str(list_rb) + str_bb)
            hundred = list_3d[0]
            decade = list_3d[1]
            unit = list_3d[2]
            sum_a = sum(list_3d[0:3])
            num = 100*hundred+10*decade+unit
            d3d=lottery.d3d.D3d(str_id,hundred,decade,unit,sum_a,num)
#             print(dc)
            result_d3d.add_result_d3d(d3d)

#     print(str(result_d3d))
    return result_d3d.get_result_d3d()

class ResultD3d(object):
    def __init__(self, result_d3d=[]):
        self.__restult_d3d = result_d3d

    def __str__(self):
        str_ret = ''
        for elem in self.__restult_d3d:
            if elem:
                str_ret += (str(elem))
        return str_ret

    def add_result_d3d(self, d3d):
        self.__restult_d3d.append(d3d)
        
    def get_result_d3d(self):
        return self.__restult_d3d


    def set_result_d3d(self, id, value):
        for elem in self.__restult_d3d:
            if id is elem.get_id():
                elem.set_d3d()

    def del_result_d3d(self):
        del self.__restult_d3d

    d3d = property(get_result_d3d, set_result_d3d, del_result_d3d, "result_d3d's docstring")
        
        
        
        
class D3d(object):

    def __init__(self, id=None, hundred=None, decade=None, unit=None, sum=None, num=None):
        self.__id = id
        self.__hundred = hundred
        self.__decade = decade
        self.__unit = unit
        self.__sum = sum
        self.__num = num
        
    def __str__(self):
        str_ret = (str(self.__id) + ' ')
        str_ret += (str(self.__hundred) + ' ')
        str_ret += (str(self.__decade) + ' ')
        str_ret += (str(self.__unit) + ' ')
        str_ret += (str(self.__sum) + ' ')
        str_ret += (str(self.__num) + ' ')
        return str_ret + '\n'
    
    def get_id(self):
        return self.__id

    def get_hundred(self):
        return self.__hundred

    def get_decade(self):
        return self.__decade

    def get_unit(self):
        return self.__unit

    def get_sum(self):
        return self.__sum

    def get_num(self):
        return self.__num

    def set_id(self, value):
        self.__id = value

    def set_hundred(self, value):
        self.__hundred = value

    def set_decade(self, value):
        self.__decade = value

    def set_unit(self, value):
        self.__unit = value

    def set_sum(self, value):
        self.__sum = value

    def set_num(self, value):
        self.__num = value

    def set_d_3d(self, value):
        self.__d3d = value

    def del_id(self):
        del self.__id

    def del_hundred(self):
        del self.__hundred

    def del_decade(self):
        del self.__decade

    def del_unit(self):
        del self.__unit

    def del_sum(self):
        del self.__sum

    def del_num(self):
        del self.__num

    id = property(get_id, set_id, del_id, "id's docstring")
    hundred = property(get_hundred, set_hundred, del_hundred, "hundred's docstring")
    decade = property(get_decade, set_decade, del_decade, "decade's docstring")
    unit = property(get_unit, set_unit, del_unit, "unit's docstring")
    sum = property(get_sum, set_sum, del_sum, "sum's docstring")
    num = property(get_num, set_num, del_num, "num's docstring")


    
