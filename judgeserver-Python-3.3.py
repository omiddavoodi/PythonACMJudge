####################################################################
#                                                                  #
#   Socket based python judge.    ----The Server----               #
#               Developed by Omid Davoodi of                       #
#        Iran University of Science and Technology                 #
#                                                                  #
####################################################################

########################################################
# Requires Python 3.3, Only tested on Windows 7 64 bit #
########################################################

###################################
# [TODO]: A "real" contest system #
###################################

############################################################################################
# Don't get fooled by the small comment above. It probably is the hardest part of the code #
############################################################################################

###########################################
# [TODO]: A Python 2.7 compatible version # 
###########################################
## no way im going back to 2.7 . do it yourself . i love 3.3 xxx

# Importing several libraries

import os, time
import socket
import random
from command import Command ## lets just organize stuff a bit and put command class in a seperated py file 
from problemConfigReader import  readProblemConfigFromFile
from serverConfigReader import readServerConfigFromFile
from participantsReader import readParticipants
from pythonSecurity import security_controller

participants = readParticipants()

s = socket.socket()         # Create a socket object
serverconfig = readServerConfigFromFile()
host = serverconfig[0]          # Get local machine name
port = serverconfig[1]          # Reserve a port for your service.
problemdict = serverconfig[3]   # The problem name dictionary
contestname = serverconfig[4]   # The name of the contest
conteststart = serverconfig[5]  # The start time of the contest
s.bind((host, port))            # Bind to the port

s.listen(1)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)

    c.send(bytearray('Connection Accepted',"ascii"))
    result = (c.recv(32768)) # Wait for the client to send the code
    problemnamesize = result[0] # The first byte of the sent data is the length of the name of the problem
    problemName = str(result[1:problemnamesize+1],"ascii") # Get the problem name

    studentIDsize = result[problemnamesize+1] # the next byte is the length of the student id
    studentID = str(result[problemnamesize+2:problemnamesize+studentIDsize+2],"ascii") # get it

    passwordsize = result[problemnamesize+studentIDsize+2] # the next byte is that of the password
    password = str(result[problemnamesize+studentIDsize+3:problemnamesize+studentIDsize+3+passwordsize],"ascii") # also get the password

    loginid = -1

    if (studentID == 'admin' and password == 'tolombe'):
        # Reload the config of the system
        participants = readParticipants()
        serverconfig = readServerConfigFromFile()
        problemdict = serverconfig[3]   # The problem name dictionary
        contestname = serverconfig[4]   # The name of the contest
        conteststart = serverconfig[5]  # The start time of the contest
    else:
        loginid = -1
        for p in range(len(participants)): # check if such id and password pair exists
            if (participants[p][0] == studentID):
                if (participants[p][2] == password):
                    loginid = p

        if (loginid != -1): # if the id and password were correct
            if (conteststart <= int(time.time())):
                print (participants[loginid][1] + ' is trying to answer the problem "' + problemName + '"')
                
                codebeginning = problemnamesize+studentIDsize+2+passwordsize
                recievedcode = str(result[codebeginning+1:],"ascii") # The code itself begins right after the password

                tempfilename = addr[0] + "." + str(random.randint(0,999)) + ".py" # We want to create a temporary file and write the code in it
                tempf = open (tempfilename, mode='w') 
                tempf.write(recievedcode)
                tempf.close()

                contestlog = open (contestname + "-Log.txt", mode='a')

                # check for secure codes. we don't want them to destroy the server
                if (security_controller(tempfilename)):           
                    # OK. We now have the code in a file. Now we should make the Command class to do the judging
                    pypath = ''
                    if (recievedcode[:4] == '#2.7'):
                        pypath = serverconfig[7]
                    else:
                        pypath = serverconfig[2]

                    command = Command([pypath, tempfilename], 1) # It sends the batch command

                    # load the config
                    try:
                        config = readProblemConfigFromFile(problemdict[problemName])
                    except:
                        config = False
                    if (config): # if there was a problem with that name
                        # run the judge
                        a = command.run(timeout = config[1] ,problem = problemdict[problemName])
                        
                        # Translate the results:
                        if (a[0] == 1): # The code ran perfectly and got accepted
                            rtsr = "Accepted!" # rtsr: 'result to send "??????"' (forgot the last part)
                            print(rtsr)
                            deltatime = int(time.time() - conteststart)
                            contestlog.write(participants[loginid][0] + "-" + problemName + "-a:" + str(deltatime) + "\n")
                        elif (a[0] == 2): # The code ran perfectly but the output was not equal to the .out file
                                          # [TODO]: A way to distinguish between presentation error and wrong answer
                            rtsr = "Wrong answer or Presentaion error!"
                            print(rtsr)
                            deltatime = int(time.time() - conteststart)
                            contestlog.write(participants[loginid][0] + "-" + problemName + "-f:" + str(deltatime) + "\n")
                        elif (a[0] == 3): # The code didn't run well. Return the error description itself
                            rtsr = "Error! : " + a[1] # a[0] = "return code", a[1] = "error desc"
                            print(rtsr)
                            deltatime = int(time.time() - conteststart)
                            contestlog.write(participants[loginid][0] + "-" + problemName + "-f:" + str(deltatime) + "\n")
                        elif (a[0] == 4): # The code took too long and so we terminated it
                            rtsr = "Time out!"
                            print(rtsr)
                            deltatime = int(time.time() - conteststart)
                            contestlog.write(participants[loginid][0] + "-" + problemName + "-f:" + str(deltatime) + "\n")
                        else:
                            rtsr = "Unknown error!" # It could be a memory limit error or something else 
                            print(rtsr)
                            deltatime = int(time.time() - conteststart)
                            contestlog.write(participants[loginid][0] + "-" + problemName + "-f:" + str(deltatime) + "\n")
                    else:
                        rtsr = "Problem not found!"
                        print(rtsr)
                else:
                    rtsr = "Illegal code pieces!"
                    print(rtsr)
                    deltatime = int(time.time() - conteststart)
                    contestlog.write(participants[loginid][0] + "-" + problemName + "-f:" + str(deltatime) + "\n")
                os.remove(tempfilename) # OK, remove that temporary file we created
                contestlog.close()
            else:
                rtsr = "Contest has not yet started!"
                print(str(addr) + " was trying to answer before the start")
        else:
            rtsr = "Username or Password is incorrect!"
            print(str(addr) + " was trying to connect with a wrong Logon")
    c.send(bytearray(rtsr,"ascii"))
    c.close()                # Close the connection
    

