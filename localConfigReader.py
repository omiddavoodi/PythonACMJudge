## extracts the config values from a CONFIG.txt  file


def readConfigFromFile():
## Return a list in form of [host,port] (both are strings)

    file = open("CONFIG.txt").readlines()
    host = "" ; port = ""; snumber = "";
    for line in file:
        ## if a line starts with '#' its a comment
        if (line[0]=='#'):
            pass
        elif("PORT" in line):
            port = line[line.find('=')+1:].strip()
        elif("HOST" in line):
            host = line[line.find('=')+1:].strip()
        elif("STUDENTNUMBER" in line):
            snumber = line[line.find('=')+1:].strip()
        elif("PASSWORD" in line):
            password = line[line.find('=')+1:].strip()
                        
    return([host,int(port),snumber,password])

