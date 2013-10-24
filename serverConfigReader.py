## extracts the config values from a CONFIG.txt  file


def readServerConfigFromFile():
## Return a list in form of [host,port] (both are strings)

    file = open("SERVERCONFIG.txt").readlines()
    host = "" ; port = ""; pythonp = ""
    for line in file:
        ## if a line starts with '#' its a comment
        if (line[0]=='#'):
            pass
        elif("PORT" in line):
            port = line[line.find('=')+1:].strip()
        elif("HOST" in line):
            host = line[line.find('=')+1:].strip()
        elif("PYTHONPATH" in line):
            pythonp = line[line.find('=')+1:].strip()
    return([host, int(port), pythonp])

