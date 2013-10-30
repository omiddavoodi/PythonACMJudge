def bmm(a, b):
    if (b == 0):
        return a
    return bmm(b, a%b)

a = []
for i in range(5):
    a.append(int(input()))

b = a[4]
for i in range(4):
    b = bmm(b, a[i])

print ("Result is " + str(b))
