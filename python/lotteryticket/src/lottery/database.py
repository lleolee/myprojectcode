# -*- coding: utf-8 -*-
#!/usr/bin/python3
# Filename: lottery.py
'''
Created on 2017年4月25日

@author: lleo
'''

import xlwt
import datetime
import lottery.d3d

def save_to_file(path, data):
    f_obj = open(path, 'wb')
    f_obj.write(bytes(data.encode('utf-8')))
    f_obj.close()    
    
def save_3d_ball_result(data_d3d):
    style_id = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
    style_red = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
    style_blue = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',num_format_str='#,##0.00')
    style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:mm:SS')
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A 3D Ball Results Sheet')
    ws.write(0, 0, datetime.datetime.now(), style_date)
    
    for i,item in enumerate(data_d3d):
        ws.write(i+1,0,str(item.get_id()),style_id)
        ws.write(i+1,1,str(item.get_hundred()),style_id)
        ws.write(i+1,2,str(item.get_decade()),style_id)
        ws.write(i+1,3,str(item.get_unit()),style_id)
        ws.write(i+1,4,str(item.get_sum()),style_id)
        ws.write(i+1,5,str(item.get_num()),style_id)
        
    wb.save('lottery_3d_ball_result.xls')
    
def save_3d_ball_frequency_sorted(frequency):
    style_id = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
    style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:mm:SS')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A 3D Results Sheet')
    ws.write(0, 0, datetime.datetime.now(), style_date)
    
    frequency_sort = sorted(frequency.items(),key=lambda x:x[1],reverse=False)
    i=1;
    for key,value in frequency_sort:
        ws.write(i,0,str(key),style_id)
        ws.write(i,1,str(value),style_id)
        i+=1
    
    wb.save('lottery_3d_ball_frequency_sort.xls')
    
def save_3d_ball_predict(num_predict):
    style_id = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
    style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:mm:SS')
    
    data_d3d_all = lottery.d3d.get_simulate_3d_all()
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A 3D Results Sheet')
    ws.write(0, 0, datetime.datetime.now(), style_date)
    
    j=0
    for i,elem in enumerate(data_d3d_all):  
        if elem.get_num() in num_predict and elem.get_sum() in range(7,20):
#             print(elem)
            ws.write(j+1,0,str(elem.get_id()),style_id)
            ws.write(j+1,1,str(elem.get_hundred()),style_id)
            ws.write(j+1,2,str(elem.get_decade()),style_id)
            ws.write(j+1,3,str(elem.get_unit()),style_id)
            ws.write(j+1,4,str(elem.get_sum()),style_id)
            ws.write(j+1,5,str(elem.get_num()),style_id)
            j+=1
    wb.save('lottery_3d_ball_predict_last100_and_sum8_20.xls')
    
class Database(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
