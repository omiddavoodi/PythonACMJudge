####################################################################
#                                                                  #
#   Socket based python judge.    ----The security----             #
#           Developed by Hooman Behnejad Fard of                   #
#        Iran University of Science and Technology                 #
#                                                                  #
####################################################################


def split(string, model):
    a = list()
    temp = ""
    for i in string:
        if i not in model:
            temp += i
        else:
            if temp == "":
                continue
            a.append(temp)
            temp = ""
    del temp
    return a


def security_controller(address_file):
    file = open(address_file, "r")
    a = file.readline()
    security = True
    while a:
        a = split(a.strip(), "#*.:;() =,+-/!><")
        if "from" in a:
            security = False
            break

        if "import" in a and a[1] != "math":
            security = False
            break

        if "__" in a:
            security = False
            break
            
        if "eval" in a:
            security = False
            break

        if "exec" in a:
            security = False
            break

        if "execfile" in a:
            security = False
            break

        if "open" in a:
            security = False
            break

        if "compile" in a:
            security = False
            break

        if "file" in a:
            security = False
            break

        a = file.readline()

    del a
    file.close()
    return security

# For testing program:
if __name__ == "__main__":
    print security_controller("security.txt")
