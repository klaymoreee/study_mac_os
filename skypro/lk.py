from random import randint
from time import *
added = input()
closed = 0
note = []
for x in added:
    if x == 'a':
        print(f'yes! it`s \'a\' under index {closed}')
        sleep(2)
        note.append(closed)
    closed += 1
for x in note:
    print(added[x])
crocs = 100
while closed > 0:
    crocs += 1
    print(str(randint(0, 11234)) * crocs)