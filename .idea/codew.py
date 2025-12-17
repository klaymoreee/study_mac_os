def duplicate_encode(word):
    y = word.lower()
    sec_str = ''
    print(y)
    for x in y:
        if y.count(x) == 1:
            sec_str += '('
        elif y.count(x) > 1:
            sec_str += ')'
    return sec_str


print(duplicate_encode('Success'))

#')())())'