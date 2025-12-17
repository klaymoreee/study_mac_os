note = [10, 10, 10, 10, 100, 100, 10, 100, 10, 100, 10, 1000, 10, 10, 1000, 1000]
note_example = [x for x in note if x != 10]
note_log = []
for x in note:
    if x == 10:
        continue
    note_log.append(x)
print(note_log)

for r, number in enumerate(note_log, start=1):
    print(r, number)
    if note_log[-1] == 1000:
        note_log.pop()
        note_log[r] = '-I kill this num\'!!!\'-'
print(*note_log)