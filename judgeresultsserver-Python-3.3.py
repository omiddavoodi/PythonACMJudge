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

import socket
import random
from serverConfigReader import readServerConfigFromFile
from participantsReader import readParticipants

participants = readParticipants()

s = socket.socket()         # Create a socket object
serverconfig = readServerConfigFromFile()
host = serverconfig[0]          # Get local machine name
port = serverconfig[1]          # Reserve a port for your service.
problemdict = serverconfig[3]   # The problem name dictionary
contestname = serverconfig[4]   # The name of the contest
s.bind((host, port))            # Bind to the port

def getContestResultTable(name, probdict, particip):
    logfile = open (name + "-Log.txt")
    log = logfile.read()
    logfile.close()

    tablewidth = 100
    colwidth = 36 // len(probdict)
    if (len(probdict) > 6):
        tablewidth = 12 * len(probdict) + 28
        colwidth = 6
    htmlcode = "<html>\n<head>\n\t<head>\n\t\t<title>" + name + \
     "</title>\n\t</head>\n\t<body>\n\t\t<center><b><font size=20>" + \
    name + ' Results</font></b></center>\n\t\t<table width="' + \
    str(tablewidth) + '%" border=2>\n\t\t\t<tr width="100%">\n\t\t\t\t' + \
    '<td width="20%" rowspan=2 colspan=2>\n\t\t\t\t\t<center>-</center>' + \
    '\n\t\t\t\t</td>'
    for i in probdict:
        htmlcode += '\n\t\t\t\t<td width="' + str(2*colwidth) + '%"' + ' colspan=2>' + \
        '\n\t\t\t\t\t<center>' + i + '</center>\n\t\t\t\t</td>'

    htmlcode += "</tr></table></body></html>"
    return htmlcode

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)

    contestlog = getContestResultTable(contestname,problemdict,participants)
    
    c.send(bytearray(contestlog,"ascii")) # Send the table

    c.close()                # Close the connection
    

