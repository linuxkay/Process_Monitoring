#!/usr/bin/python2.7
import commands
import os
while True:
  output = commands.getoutput('ps -aux')
  if '/usr/bin/python2.7 /home/user/Workspace/silenceisgolden.py' in output:
#    print "ITS ALIVE!!!"
    continue 
  else: 
    os.system('/usr/bin/python2.7 /home/user/Workspace/silenceisgolden.py &')
