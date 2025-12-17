amt_suv = 75
amt_less = 112
amt_total_1, amt_total_2 = int(input()), int(input())
amt_weight = (amt_total_1 * amt_suv) + (amt_total_2 * amt_less)
print(round(amt_weight / 1000, 2))