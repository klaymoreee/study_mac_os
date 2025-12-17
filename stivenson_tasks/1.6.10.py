#library part
from math import *

#data & input part
opers = ['+','-','%','*','/','log10','**']
data_note = [int(input('Type first number: ')),
             int(input('Type second number: ')),
             input('Type operand: ')]

#math part
res = 0
for x in opers:
    if data_note[2] == x:
        if data_note[2] == 'log10':
            res = log10(data_note[0])
        else: res = eval(f'{data_note[0]} {data_note[2]} {data_note[1]}')
for x in str(res):
    if '.' in str(res):
        if len(str(res)[str(res).index('.'):]) <= 2:
            res = round(res)
        else:
            res = round(res, 2)
            
#output part
print(res)
         





        
        
        

