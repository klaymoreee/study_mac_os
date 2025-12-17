request_us = int(input())
above = 0.15
under = 0.18
money_summ = request_us * under * above
print(round(request_us + money_summ, 2), above, under)