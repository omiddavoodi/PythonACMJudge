#2.7
def digit_to_char(digit):
    if digit < 10: return chr(ord('0') + digit)
    else: return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)

        
def int2str(num, base=16, sbl=None):
    if not sbl:
        sbl = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    neg = False
    if num < 0:
        neg = True
        num = -num

    num, rem = divmod(num, base)
    ret = ''
    while num:
        ret = sbl[rem] + ret
        num, rem = divmod(num, base)
    ret = ('-' if neg else '') + sbl[rem] + ret

    return ret
x = int(raw_input())
for i in range(x):
    print int2str(int(raw_input()), int(raw_input()))
