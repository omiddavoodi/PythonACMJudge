#3.3
def fib(n):
    l =[1,1]
    i = 0
    while ( i != n-2):
        temp = l[1]
        l[1] = l[1] + l[0]
        l[0] = temp
        i += 1
    result = str(l[1])
    print (result[-5:] + result[:5])

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1)+ fib1(n-2)
    
a = int(input())

for i in range(a):
    fib(int(input()))
