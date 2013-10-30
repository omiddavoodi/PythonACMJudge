def func(string):
    a = 0
    for i in range(len(string)):
        a += i * ord(string[i])
    print (a)


a = int(input())

for i in range(a):
    func(input())

