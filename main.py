
x = int(input())

count = []
count_inc = []
rest = 0
index_co = 0
for i in range(x):
    count.append(i)
    
for y in count:
    if y % 2 == 0 and y > 0 and y % 10 != 2:
        rest += 1
        count_inc.append(y)
note = [u for u in count_inc if u % 10 == 6]

for j in range(len(count) - 3):
    if (count[j] + count[j + 1]) < (count[j + 2] + count[j + 3]): 
        index_co += 1                                                          #j[0]  j[1]  j[2]       
print(rest, count_inc, "              ___ ", note,'--------' ,index_co, "- счетчик")
     