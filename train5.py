slut = []
for x in range(3):
    slut.append(int(input()))
count = 0
if slut[0] >= 2:
    count += 1
if slut[1] >= 50000:
    count += 1
if slut[2] >= 2:
    count += 1
print(f"Ваш кредитный рейтинг - {count}")