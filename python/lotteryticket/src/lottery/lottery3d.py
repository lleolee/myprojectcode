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
import lottery.d3d
from numpy import sort
from lottery import database


def d3d_result_classify(data_d3d):
    d3d_classify = {}
    for i,elem in enumerate(data_d3d):
        if elem.get_num() not in d3d_classify:
            d3d_classify[elem.get_num()]=[]
        d3d_classify[elem.get_num()].append(elem)
    return d3d_classify
        
def sum_result_classify(data_d3d):
    d3d_classify_sum = {}
    for i,elem in enumerate(data_d3d):
        if elem.get_sum() not in d3d_classify_sum:
            d3d_classify_sum[elem.get_sum()]=[]
        d3d_classify_sum[elem.get_sum()].append(elem)
    return d3d_classify_sum
        
def get_frequency(count,classify):
    frequency = {}
    if count < len(classify):
        print('count is too short')
        return None
    for i in range(count):
        frequency[i] = 0
    for key,value in sorted(classify.items()):
        frequency[key] = len(value)
    return frequency


print('get 3d data')
data_d3d = lottery.d3d.get_lottery_3d()
#save to xls
database.save_3d_ball_result(data_d3d)

print('classify')
classify = d3d_result_classify(data_d3d)
classify_sum = sum_result_classify(data_d3d)

frequency = get_frequency(1000, classify)
#save sorted frequency
database.save_3d_ball_frequency_sorted(frequency)

frequency_sum = get_frequency(30, classify_sum)

frequency_sort = sorted(frequency.items(),key=lambda x:x[1],reverse=False)

print(frequency_sort)
num_last = []
# for key,value in frequency_sort[0:100]:
for key,value in frequency_sort:
    if value in range(1,6):
#     print('total:'+ str(len(data_d3d))+' '+str(key)+' '+str(value))
        num_last.append(key)

# simulate_3d_all = lottery.d3d.get_simulate_3d_all()
# d3d_classify_sum_all = sum_result_classify(simulate_3d_all)
#      
# sum_frequency_all = get_frequency(30, d3d_classify_sum_all)
# # print(sum_frequency_all)
# percent = [(x,float(y/1000.0)) for x,y in sum_frequency_all.items()]
# sum_percent = 0
# for x,y in percent:
#     print('sum='+str(x)+' percent='+str(y))
#     if x in range(7,21):
#         sum_percent +=y
# print('sum='+str([i for i in range(7,21)])+' sum_percent='+str(sum_percent))
    

print('the result of last frequency & last sum saving')
database.save_3d_ball_predict(num_last)

style_id = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
style_date = xlwt.easyxf(num_format_str='YYYY-MM-DD HH:mm:SS')
wb = xlwt.Workbook()
ws = wb.add_sheet('A 3D Results Sheet')
ws.write(0, 0, datetime.datetime.now(), style_date)

predict_statistc = []
max = 1000 if len(data_d3d) > 1000 else len(data_d3d)
for i in range(max):
    lucky_3d = data_d3d[-(i+1)]
    ws.write(i+1,0,str(lucky_3d.get_id()),style_id)
    ws.write(i+1,1,str(lucky_3d.get_num()),style_id)
    ws.write(i+1,2,str(lucky_3d.get_sum()),style_id)
#     print(data_d3d[-(i+1)])
#     print([x.get_num() for x in data_d3d[:-(i+1)]])
    classify = d3d_result_classify(data_d3d[:-(i+1)])
    frequency = get_frequency(1000, classify)
    frequency_sort = sorted(frequency.items(),key=lambda x:x[1],reverse=False)
#     print(frequency_sort)
    for key,value in frequency_sort:
        if key == lucky_3d.get_num():
#             print(value)
            ws.write(i+1,3,str(value),style_id)
#             print(frequency_sort.index((key,value)))
            ws.write(i+1,4,str(frequency_sort.index((key,value))),style_id)
            predict_statistc.append((lucky_3d.get_id(),lucky_3d.get_num(), \
                                   lucky_3d.get_sum(),value,frequency_sort.index((key,value))))
            
    if i%100 is 0:
        print(i)
        
wb.save('lottery_3d_predict_statistic.xls')
# print(predict_statistc)

def predict_sum_classify(predict):
    sum_classify = {}
    for i,elem in enumerate(predict):
        if elem[2] not in sum_classify:
            sum_classify[elem[2]]=[]
        sum_classify[elem[2]].append(elem)
    return sum_classify
         
def predict_f(predict):
    classify_f = {}
    for i,elem in enumerate(predict):
        if elem[3] not in classify_f:
            classify_f[elem[3]]=[]
        classify_f[elem[3]].append(elem[3])
    return classify_f

def predict_rank(predict):
    classify_rank = {}
    for i,elem in enumerate(predict):
        if elem[4] not in classify_rank:
            classify_rank[elem[4]]=[]
        classify_rank[elem[4]].append(elem[4])
    return classify_rank

print('classify predict')
sum_predict_classify = predict_sum_classify(predict_statistc)
# print(sum_predict_classify)
sum_predict_frequency = get_frequency(30, sum_predict_classify)
# print(sum_predict_frequency)
sum_predict_percent = [(x,float(y/len(predict_statistc))) for x,y in sum_predict_frequency.items()]
# print(sum_predict_percent)
sum_percent = 0
for x,y in sum_predict_percent:
    print('sum='+str(x)+' percent='+str(y))
    if x in range(7,20):
        sum_percent +=y
print('sum='+str([i for i in range(7,20)])+' sum_percent='+str(sum_percent))

f_predict_classify = predict_f(predict_statistc)
# print(f_predict_classify)
f_predict_frequency = get_frequency(16, f_predict_classify)
# print(f_predict_frequency)
sum_predict_percent = [(x,float(y/len(predict_statistc))) for x,y in f_predict_frequency.items()]
# print(sum_predict_percent)
sum_percent = 0
for x,y in sum_predict_percent:
    print('f='+str(x)+' percent='+str(y))
    if x in range(1,6):
        sum_percent +=y
print('f='+str([i for i in range(1,6)])+' f_percent='+str(sum_percent))

rank_predict_classify = predict_rank(predict_statistc)
# print(rank_predict_classify)
rank_predict_frequency = get_frequency(1000, rank_predict_classify)
# print(rank_predict_frequency)
rank_predict_percent = [(x,float(y/len(predict_statistc))) for x,y in rank_predict_frequency.items()]
# print(rank_predict_percent)
sum_percent = 0
for x,y in rank_predict_percent:
#     print('rank='+str(x)+' percent='+str(y))
    if x in range(200,900):
        sum_percent +=y
# print('rank='+str([i for i in range(200,800)])+' rank_percent='+str(sum_percent))
print('rank_percent='+str(sum_percent))

odd_even_3d = []
for i,elem in enumerate(data_d3d):
    oe_h = elem.get_hundred()%2
    oe_d = elem.get_decade()%2
    oe_u = elem.get_unit()%2
    oe_s = elem.get_sum()%2
    oe_n = elem.get_num()%2
    oe = oe_h*100+oe_d*10+oe_u
    odd_even_3d.append((elem.get_id(),oe_h,oe_d,oe_u,oe_s,oe_n,oe))  

sum_h = 0
sum_d = 0
sum_u = 0
sum_s = 0
sum_n = 0
oe_classify = {}
for id,h,d,u,s,n,oe in odd_even_3d:
    if h:
        sum_h+=1
    if d:
        sum_d+=1
    if u:
        sum_u+=1
    if s:
        sum_s+=1
    if n:
        sum_n+=1
    if oe not in oe_classify:
        oe_classify[oe] = []
    oe_classify[oe].append((id,h,d,u,s,n,oe))
    
count = [0,1,10,11,100,101,110,111]
oe_frequency = {}
for i in count:
    oe_frequency[i] = (0,0)
for key,value in oe_classify.items():
    oe_frequency[key] = (len(value),float(len(value)/len(odd_even_3d)))
# print(oe_frequency)
for key,value in oe_frequency.items():
    print('percent oe '+str(key)+' is '+str(value[1]))
    
print('percent odd&even hundred is '+str(float(sum_h/len(odd_even_3d))))
print('percent odd&even decade is '+str(float(sum_d/len(odd_even_3d))))
print('percent odd&even unit is '+str(float(sum_u/len(odd_even_3d))))
print('percent odd&even sum is '+str(float(sum_s/len(odd_even_3d))))
print('percent odd&even num is '+str(float(sum_n/len(odd_even_3d))))
        



    