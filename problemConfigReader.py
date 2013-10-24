import os

def readProblemConfigFromFile(problemName):
    problemfilepath = "problems/" +problemName+".conf"
    if (os.path.isfile(problemfilepath)):
        file = open(problemfilepath).readlines()
        desc = "";timeout = ""
        for line in file:
            ## if a line starts with '#' its a comment
            if (line[0]=='#'):
                pass
            elif("TIMEOUT" in line):
                timeout = line[line.find('=')+1:].strip()
            elif("DESC" in line):
                desc = line[line.find('=')+1:].strip()
        return([desc,int(timeout)])
    return (False)
