all_money_sumz = []
impact_us = float(input())
impact_total = 0
for x in range(3):
    impact_total = impact_us * 0.4
    impact_us += impact_total
    all_money_sumz.append(round(impact_us, 2))
print(*all_money_sumz, sep = '\n')