r = float(input())

num_p = 3.14

area = num_p * (r ** 2)
volume = (4 / 3) * (num_p * (r ** 2))


for x in str(area):
    if len(str(area[str(area).index('.'):])) >= 2:
        area = round(area, 2)
for x in str(volume):
    if len(str(volume[str(volume).index('.'):])) >= 2:
        volume = round(volume, 2)
        
print(area, volume)