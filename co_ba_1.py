from typing import List, Dict

def solution(words: List[str]) -> List[str]:
    counter = 0
    for x in words:
        cunt = 0
        for i in x:
            if i in 'aeiouy':                        #['a', 'e', 'i', 'o', 'u', 'y']
                x = x.replace(i, str(cunt), 1)
                words[counter] = x
            cunt += 1
        counter += 1
    return words

print(solution(['wuidqpwiuond', 'wdqwdqwd', 'ooooooooo']))