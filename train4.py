select = []
select.append(input())
select.append(input())
count = 0

for x in select:
    print(x)
    if 'р' in x:
        count += 1
print(count, select)


