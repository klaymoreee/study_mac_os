num_us = int(input())
plus_summ = ((num_us)*(num_us + 1)) / 2
print(plus_summ)

summ = 0

for x in range(1, num_us + 1):
    if x > 0:
        summ += x
print(summ)