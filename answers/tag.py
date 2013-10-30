#3.3
a = input()
i = 0
flag = False
result = ""
while(i != len(a)):
    if(a[i] != "<" and not flag):
        result += a[i]
    elif (a[i] == "<"):
        flag = True
    elif (a[i] == ">" and flag):
        flag = False
    i += 1
    
print (result)


    
