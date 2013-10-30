import math
a = float(input())
while a >= 0.0:
    g = str(math.sqrt(a))
    print (g[:g.find('.')+5])
    a = float(input())
