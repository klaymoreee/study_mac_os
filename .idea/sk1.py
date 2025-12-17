letters_1 = ["A", "B", "C", "D"]
letters_2 = ["E", "F", "G", "K", "L", "M", "N"]

print(letters_2[::-1])

count = int(input())

addition = letters_2[:count]

letters_1.extend(addition)

# Не удаляйте код ниже, он нужен для проверки

print("".join(letters_1))

stroke = '2313123'

calculate = 0

for x in stroke:
    calculate += int(x)
    
print(calculate)