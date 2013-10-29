####################################################################
#                                                                  #
#   Socket based python judge.    ----The Results Server----       #
#               Developed by Omid Davoodi of                       #
#        Iran University of Science and Technology                 #
#                                                                  #
####################################################################

########################################################
# Requires Python 3.3, Only tested on Windows 7 64 bit #
########################################################

# Importing several libraries

import socket, os, time
import random
from serverConfigReader import readServerConfigFromFile
from participantsReader import readParticipants

participants = readParticipants()

s = socket.socket()         # Create a socket object
serverconfig = readServerConfigFromFile()
host = serverconfig[0]          # Get local machine name
port = serverconfig[1] + 1      # Reserve a port for your service.
problemdict = serverconfig[3]   # The problem name dictionary
contestname = serverconfig[4]   # The name of the contest
penaltytime = serverconfig[6]   # The penalty for failing in an attempt
s.bind((host, port))            # Bind to the port

cachetime = 0
cachedhtml = ''
# Omid's comments:
# this function creates an html file based on the current situation using the contest's log file
# it cahces the result until the log file is updated
# unfortunately, right now i'm too lazy to comment this out as much as i have done the others
def getContestResultTable(name, probdict, particip):
    global cachetime
    global cachedhtml
    
    lastupdate = os.path.getmtime(name + "-Log.txt")

    if (cachetime < lastupdate): #check if the log file is updated. if not, use the cache
        cachetime = lastupdate
        
        logfile = open (name + "-Log.txt")
        log = logfile.readlines()
        logfile.close()

        problist = []

        for i in probdict: # create a list of the problems
            problist.append(i)

        problist.sort()

        tablewidth = 100
        colwidth = 36 // len(probdict)

        
        if (len(probdict) > 6):
            tablewidth = 12 * len(probdict) + 28
            colwidth = 6
        htmlcode = "<html>\n\t<head>\n\t\t<title>" + name + \
         "</title>\n\t</head>\n\t<body>\n\t\t<center><b><font size=20>" + \
        name + ' Results</font></b></center>\n\t\t<table width="' + \
        str(tablewidth) + '%" border=2>\n\t\t\t<tr width="100%">\n\t\t\t\t' + \
        '<td width="20%" rowspan=2 colspan=2>\n\t\t\t\t\t<center>-</center>' + \
        '\n\t\t\t\t</td>'
        for i in problist:
            htmlcode += '\n\t\t\t\t<td width="' + str(2*colwidth) + '%"' + ' colspan=2>' + \
            '\n\t\t\t\t\t<center>' + i.upper() + '</center>\n\t\t\t\t</td>'

        htmlcode += '<td width="8%" rowspan=2 colspan=2>\n\t\t\t\t\t<center>Penalty' + \
                    '</center>\n\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr width="100%">\n'
        
        for i in range(len(probdict)):
            htmlcode += '\n\t\t\t\t<td width="' + str(colwidth) + '%">' + \
            '\n\t\t\t\t\t<font size=1><center>Accepted</center></font>' + \
            '\n\t\t\t\t</td>\n\t\t\t\t<td width="' + str(colwidth) + '%">' + \
            '\n\t\t\t\t\t<font size=1><center>Failed</center></font>' + \
            '\n\t\t\t\t</td>'

        htmlcode += '\n\t\t\t</tr>'

        scores = {}
        numparticipants = len(particip)

        # from this part until ---||||---- it is trying to sort the contestants properly
        
        for i in range(numparticipants):
            scores[particip[i][0]] = [0,[],{}]
            for j in probdict:
                scores[particip[i][0]][2][j] = 0
                
        for line in log:
            if (line.find('-') != -1):
                uid = line[:line.find('-')]
                pname = line[line.find('-')+1:line.rfind('-')]
                res = line[line.rfind('-')+1:line.rfind(':')]
                tim = int(line[line.rfind(':')+1:].strip())

                if pname not in scores[uid][1]:
                    if res == 'a':
                            scores[uid][1].append(pname)
                            scores[uid][0] += tim
                    else:
                        scores[uid][0] += penaltytime
                        scores[uid][2][pname] += 1

        unsorted = []
        for i in range(numparticipants):
            unsorted.append([scores[particip[i][0]][0], len(scores[particip[i][0]][1]), i, particip[i][0]])
            
        for i in range(1, numparticipants):
            for j in range(i):
                if unsorted[i][1] > unsorted[j][1]:
                    unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
                elif unsorted[i][1] == unsorted[j][1] and unsorted[i][0] < unsorted[j][0]:
                    unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
                elif unsorted[i][1] == unsorted[j][1] and unsorted[i][0] == unsorted[j][0]:
                    unsorted[j][2] = unsorted[i][2]

        # ----||||----

        for i in range(numparticipants): # ok. now that they are sorted, print them out
            b = i + 1
            for k in range(0,i):
                if (unsorted[k][2] == unsorted[i][2]):
                    b -= 1
                else:
                    break

            uname = ""
            for l in particip:
                if l[0] == unsorted[i][3]:
                    uname = l[1]
                    break
            
            htmlcode += '\n\t\t\t<tr width="100%">\n\t\t\t\t<td width="3%">' + \
            '\n\t\t\t\t\t<center>' + str(b) + '</center>\n\t\t\t\t</td>\n\t\t\t\t' + \
            '<td width="17%">\n\t\t\t\t\t<center>' + uname + '</center>\n\t\t\t\t</td>'
            for j in problist:
                htmlcode += '\n\t\t\t\t<td width="' + str(colwidth) + \
                '%">\n\t\t\t\t\t<center>'
                
                if (j in scores[unsorted[i][3]][1]):
                    htmlcode += "Yes"
                else:
                    htmlcode += "No"

                htmlcode += '</center>\n\t\t\t\t</td>\n\t\t\t\t<td width="' + \
                str(colwidth) + '%">\n\t\t\t\t\t<center>' + str(scores[unsorted[i][3]][2][j]) + \
                '</center>\n\t\t\t\t</td>'
            
            htmlcode += '\n\t\t\t\t<td width="8%">\n\t\t\t\t\t<center>' + \
            str(scores[unsorted[i][3]][0]) + '</center>\n\t\t\t\t</td>\n\t\t\t</tr>'
        
        htmlcode += "\n\t\t</table>\n\t</body>\n</html>"
        cachedhtml = htmlcode
        
    else:
        htmlcode = cachedhtml
        
    return htmlcode

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)

    contestlog = getContestResultTable(contestname,problemdict,participants)

    # send the html code for them to create a file with
    c.send(bytearray(contestlog,"ascii")) # Send the table

    c.close()                # Close the connection
    

