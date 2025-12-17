word = input()

has_r = 'r' in word
has_l = 'l' in word
has_s = 's' in word

print(f'Слово {word}')

if has_r == True:
    print('Есть буква R')
if has_l == True:
    print('Есть буква L')
if has_s == True:
    print("Есть буква S")