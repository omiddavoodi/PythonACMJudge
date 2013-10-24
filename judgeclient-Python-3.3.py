####################################################################
#                                                                  #
#   Socket based python judge.    ----The Client----               #
#      Developed by Omid Davoodi and Mohammad Reza Barazesh of     #
#        Iran University of Science and Technology                 #
#                                                                  #
####################################################################

########################################################
# Requires Python 3.3, Only tested on Windows 7 64 bit #
########################################################

#######################################################################
# [TODO][IMPORTANT]: A Python 2.7 compatible version [IMPORTANT][TODO]#
#######################################################################

###################################
# [TODO]: A "real" contest system #
###################################

############################################################################################
# Don't get fooled by the small comment above. It probably is the hardest part of the code #
############################################################################################

import socket               # Import socket module
import os
from localConfigReader import readConfigFromFile

# A little bit of introducing
print ("        In         the         name         of         Allah")
print ("                   -Python   Judge   Client-") # [TODO]:Choose a better name like "PyJudge" or a joking, irrelevant one like "Bastani"                             
print ("                Developed     by     Omid Davoodi") 
print ("                    And Mohammad Reza Barazesh") # Of course until someone else contributes
print ("            Iran University of Science and Technology") # Which probably suggests what a mess this app is
print ("        ===================================================== \n") 


## [TODO] : lets get the student's number too ?
file = ""
while(not os.path.isfile(file)):
    file = input("Please enter the name of the python file(eg. reverse.py):")
    if(not os.path.isfile(file)) : print ("WRONG FILE NAME")


# [TODO]: Should change to A, B, C, D, etc. when we implement a real contest system

problem = input("Please enter the name of the problem(eg. 00002):")

# Open the code file and read its contents
try :
    print("Open the file "+file+"...",end="")
    ff = open(file)
    code = ff.read()
    ff.close()
    print("OK!")
except:
    print ("An error occured while trying to read the file . file not found or access error !")
    
try:
    print("Creating a socket...",end="")
    s = socket.socket()         # Create a socket object
    print("OK!")
except:
    print("Error creating a socket object !")

# If you want to test it in a real network, simply put the IP of the server like this "host = '192.168.1.3'"
# Done ! [TODO]: A config file to write the IP in it as this will get to the hands of students as a compiled app.
try:
    print("Reading the config.txt file...",end="") 
    config = readConfigFromFile()
    host = config [0]
    port = config [1]
    sid = config [2]
    password = config [3]
    print("OK!")
except:
    print("Error reading the config.txt file !")


try:
    print("Connecting to the server ("+host+":"+str(port)+") ...",end="")
    s.connect((host, port))
    # Print the 'Connection Accepted' message
    print (str(s.recv(32768),"ascii"))
    print("OK!")
except:
    print("Connecting to server failed !")

try:
    print("Sending the data...")
    # Send: length of the name of the problem: 1 byte, name of the problem, unknown bytes, student number: 3 bytes, length of password: 1 byte, password: unknown bytes, the code: unknown bytes
    # Note that the server recieves up to 32768 bytes (32kb) of data each turn, meaning that codes more than about 32kb will cause errors
    s.send(bytearray(chr(len(problem)) + problem + chr(len(sid)) + sid + chr(len(password)) + password + code,"ascii"))
    # Print the result we get from the server (eg. Accepted, Wrong answer, etc.)
    print ("Result:"+str(s.recv(32768),"ascii"))
    print("OK!")
except:
    print("Error sending the data to the server !")

s.close                     # Close the socket when done

# Done(?)The user should be able to see what he has done. [TODO]: Logging the whole process is not a bad idea
input()

##[TODO] changing the file to .pyc might not be a bad idea :)
