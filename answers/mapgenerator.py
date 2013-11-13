f = open('input.txt', 'w')
from random import randrange
count = 0
f.write('@' * 80 + '\n')
for i in range(20):
    f.write('@')
    for j in range(78):
        f.write('@' if randrange(0,3) % 2 == 1 else '#')
    f.write('@\n')
    
f.write('@' * 80)
f.close()
