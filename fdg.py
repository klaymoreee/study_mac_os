from operator import index
from typing import List, Dict


words = ['solongword', 'wowsolongword', 'wowsomuchlongword']
counter = 0

for x in words:
    cunt = 0
    print(x)
    for i in x:
        print(i)
        if i in 'aeiouy':                        #['a', 'e', 'i', 'o', 'u', 'y']
            x = x.replace(i, str(cunt), 1)
            print('---', i, '----', x)
            words[counter] = x
        cunt += 1
    print(counter, x)
    counter += 1
print(words)

