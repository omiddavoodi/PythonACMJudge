#2.7
"""
l = [['@','@','@','@','@','@','@'],
     ['@','#','@','@','@','#','@'],
     ['@','#','@','#','@','#','@'],
     ['@','#','@','@','@','#','@'],
     ['@','C','#','#','#','#','@'],
     ['@','#','#','#','#','#','@'],
     ['@','@','@','@','@','@','@']]
"""
l = [[]]
a = int(raw_input())
for i in range(a):
    temp = raw_input()
    for j in temp:
        l[-1].append(j)
    l.appen([])
    
h = len(l)
w = len(l[1])
pos = (0,0)
for i in range(h):
    for j in range(w):
        if l[i][j] == 'C':
            pos = (i, j)
            break
        
def paint(l, pos):
    x = pos[0]
    Y = pos[1]
    if l[x][Y] != '@':
        l[x][Y] = 'C'
        
        if (x - 1 >= 0) and l[x - 1][Y] != 'C':
            paint(l, (x - 1, Y))
            
        if (Y - 1 >= 0) and l[x][Y - 1] != 'C':
            paint(l, (x, Y - 1))

        if (x+1 < h) and l[x + 1][Y] != 'C':
            paint(l, (x + 1, Y))
            
        if (Y+1 < w) and l[x][Y + 1] != 'C':
            paint(l, (x, Y + 1))


paint(l, pos)
for i in range(a):
    for j in range(len(l[2])):
        if j != len(len(l[2])):
            print [i][j],
        else print [i][j]
