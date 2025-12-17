time = {'days' : int(input()),
        'hours' : int(input()),
        'minute' : int(input()),
        'seconds' : int(input())}
time_summ = 0

if time['days'] > 0:
    time_summ += time['days'] * 86400
if time['hours'] > 0:
    time_summ += time['hours'] * 3600
if time['minute'] > 0:
    time_summ += time['minute'] * 60
if time['seconds'] > 0:
    time_summ += time['seconds']
    
print(time_summ)