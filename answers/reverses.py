def rev(string):
    string  = string.split(" ")
    temp = ""
    for i in string:
        temp += i[::-1] + " "
    print temp
    

        
a =int(raw_input())

for i in range(a):
    rev(raw_input())
