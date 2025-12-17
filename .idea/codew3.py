def filter_list(l):
    new_l = []
    for x in l:
        if type(x) == int:
            new_l.append(x)
    return new_l
    

print(filter_list([1,2,'a','b']))
            