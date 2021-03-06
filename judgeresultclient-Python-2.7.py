####################################################################
#                                                                  #
#   Socket based python judge.    ----The Result Client----        #
#                   Developed by Omid Davoodi                      #
#        Iran University of Science and Technology                 #
#                                                                  #
####################################################################

########################################################
# Requires Python 3.3, Only tested on Windows 7 64 bit #
########################################################

#######################################################################
# [TODO][IMPORTANT]: A Python 2.7 compatible version [IMPORTANT][TODO]#
#######################################################################

import socket               # Import socket module
from localConfigReader import readConfigFromFile

try:
    print "Creating a socket...",
    s = socket.socket()         # Create a socket object
    print("OK!")
except:
    print("Error creating a socket object !")

try:
    print "Reading the config.txt file...", 
    config = readConfigFromFile()
    host = config [0]
    port = config [1] + 1
    print("OK!")
except:
    print("Error reading the config.txt file !")

try:
    print "Connecting to the server ("+host+":"+str(port)+") ...",
    s.connect((host, port))
    # update the html file
    table = s.recv(32768)
    htmlfile = open ("Results.html", mode = 'w')
    htmlfile.write(table)
    htmlfile.close()
    print("OK!")
except:
    print("Connecting to server or writing the file failed !")

s.close                     # Close the socket when done
