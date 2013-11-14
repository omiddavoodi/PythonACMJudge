#2.7
n = 3#int(raw_input())
a=[i*i for i in range(n*n)]
b=[i*i for i in range(n*n)]
c = [0 for i in range(n*n)]

indexa = 0
indexb = 0
indexc = 0      
for i in range(n):
    for j in range(n):
        for i in range(n):
            c[indexc] += a[indexa + i]*b[indexb + i]
        indexc += 1
        indexb += n
    indexb -= n*n
    indexa += n
temp = ""
for i in range(n):
    for j in range(n):
        temp += str(c[n*i + j])
    if i != n-1:
        temp += '\n'
print temp
