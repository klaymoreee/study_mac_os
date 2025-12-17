from string import digits

def validate_pin(pin):
    tr_am = 0
    if len(pin) == 6 or len(pin) == 4:
        for x in pin:
            if x in digits:
                tr_am += 1
    if tr_am == len(pin):
        return True
    else: return False

print(validate_pin(''))