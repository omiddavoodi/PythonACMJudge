#3.3
def bmm(a, b):
    (c, d) = (a, b)
    while d !=0:
        (c, d) = (d, c%d)
    return c

a = []
for i in range(5):
    a.append(int(input()))

b = a[4]
for i in range(4):
    b = bmm(b, a[i])

print ("Result is " + str(b))
