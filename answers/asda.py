from subprocess import Popen
ooo =open("pashmak.txt", "w")
oo = open("pashmakerror.txt", "w")
Popen("E:/Program Files/Python27/python.exe paint.py",
      stdin=open("E:\GitHub\PythonACMJudge - Copy\problems\00010.in"),
      stderr=oo,
      stdout=ooo).communicate()

ooo.close()
oo.close()
