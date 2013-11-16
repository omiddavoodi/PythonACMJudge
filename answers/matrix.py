#2.7
n = int(raw_input())
a = []
b = []
for i in range(n*n):
    a.append(int(raw_input()))
for i in range(n*n):
    b.append(int(raw_input()))

c = [0 for i in range(n*n)]

indexa = 0
indexb = 0
indexc = 0      
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[indexc] += a[indexa + k]*b[indexb + k*n]
        indexc += 1
        indexb += 1
    indexb = 0
    indexa += n
temp = ""
for i in range(n):
    for j in range(n):
        temp += str(c[n*i + j])
    if i != n-1:
        temp += '\n'
print temp
