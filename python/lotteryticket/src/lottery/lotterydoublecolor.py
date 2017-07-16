'''
Created on 2017年5月29日

@author: lleo
'''
import urllib
import re
import bs4
import xlwt
import datetime

import lottery.web 
import lottery.double_color


def get_lottery_double_color():
#     url='http://trend.caipiao.163.com/ssq/?beginPeriod=2012030&endPeriod=2017061'
    url='http://trend.caipiao.163.com/ssq/?periodNumber=100'
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
            print('read data OK\n')           
#             print('read data OK\n'+str(data))
        else:
            return None
    
    bs = bs4.BeautifulSoup(data, 'html.parser')
    result_dc=lottery.double_color.ResultDoubleColor()
    for child_tr in bs.body.tbody.children:
        str_id = ''
        list_rb = []
        str_bb = ''
        
        if child_tr:
            for child_td in child_tr:
#                 print(child_td)
                
                td_id = re.compile(r'<td>(.{7})</td>')
                id = td_id.findall(str(child_td))
                if id:
                    str_id = str(id[0])
#                     print('#####id######'+str(id))
                td_red = re.compile(r'<td class="ball_[rb][er][do].*?>(.*?)</td>')
                red_ball = td_red.findall(str(child_td))
                if red_ball:
                    list_rb.append(str(red_ball[0]))
#                     print('#####red######'+str(red_ball))
                td_blue = re.compile(r'<td class="ball_blue js-fold".*?>(.*?)</td>')
                blue_ball = td_blue.findall(str(child_td))
                if blue_ball:
                    str_bb = str(blue_ball[0])
#                     print('#####blue######'+str(blue_ball))
        if list_rb:
#             print(str_id + str(list_rb) + str_bb)
            dc=lottery.double_color.DoubleColor(str_id,list_rb,str_bb)
#             print(dc)
            result_dc.add_result_double_color(dc)

    print(str(result_dc))
    style_id = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
    style_red = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
    style_blue = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',num_format_str='#,##0.00')
    style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:mm:SS')
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Double Color Results Sheet')
    ws.write(0, 0, datetime.datetime.now(), style_date)
    
    for i,item in enumerate(result_dc.get_result_double_color()):
        ws.write(i+1,0,str(item.get_id()),style_id)
        for j,item_j in enumerate(item.get_red()):
            ws.write(i+1,j+1,item_j,style_red)
        ws.write(i+1,7,item.get_blue(),style_blue)
#     ws.write(2, 0, 1)
#     ws.write(2, 1, 1)
#     ws.write(2, 2, xlwt.Formula("A3+B3"))
 
    wb.save('lottery_double_color_ball.xls')
    return result_dc.get_result_double_color()

get_lottery_double_color()