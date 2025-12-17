#module part
from math import *

#input part
t_1, g_1 = radians(float(input())), radians(float(input()))
t_2, g_2 = radians(float(input())), radians(float(input()))

#calculate part
formul = eval(f'{6371.01} {'*'} acos({sin(t_1) * sin(t_2) + cos(t_1) * cos(t_2) * cos(g_1 - g_2)})')
print(round(formul, 2))


