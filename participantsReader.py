## extracts the config values from a CONFIG.txt  file
import copy

def readParticipants():
## Return a list in form of [host,port] (both are strings)

    file = open("SERVERPARTICIPANTS.txt").readlines()
    parts = []
    for line in file:
        temp = list()
        temp.append(line[:line.find(':')].strip())
        temp.append(line[line.find(':')+1:line.rfind(':')].strip())
        temp.append(line[line.rfind(':')+1:].strip())
        parts.append(copy.deepcopy(temp))
    return(parts)

