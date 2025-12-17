from math import *

s = int(input())
n = int(input())
n_p = 3.14

area = (n * (s ** 2)) / (4 * tan(n_p / n))
print(area) 