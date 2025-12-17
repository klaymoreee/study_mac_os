def generate_hashtag(s):
    if s == '':
        return False
    nrt_list = []
    newest_list = []
    new_list = s.split()
    for x in new_list:
        x = x.lower()
        newest_list.append(x)
    for y in newest_list:
        y = y[0].upper() + y[1:]
        nrt_list.append(y)
    new_str = '#' + ''.join(nrt_list)
    if len(new_str) > 140:
        return False
    return new_str

print(generate_hashtag('Codewars Is Nice'))
    