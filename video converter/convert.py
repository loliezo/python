import os
from time import sleep
from winsound import MessageBeep

plac = os.getcwd()
place = str.join('',plac)
print place
lsdir = os.listdir(place)
print lsdir
conten = str.join(' ',lsdir)
print conten
contentt = conten.strip(' convert.py stuf Thumbs.db')
print contentt
content = contentt.split(" ")
print content
try:    command = 'stuf\media.exe ' + contentt + ' --sout #gather:std{access=file,dst=3.avi} --sout-keep --play-and-exit --intf dummy'
except IndexError: command = 'stuf\media.exe ' + content[0] + ' ' + content[1] + ' --sout #gather:std{access=file,dst=3.avi} --sout-keep --play-and-exit'
print command
os.system(command)
print 'test'
brake = 'stuf\Handbrake\HandBrakeCLI.exe -i 3.avi -o content.m4v'
os.system(brake)
os.remove('3.avi')
print 'finish'
MessageBeep()
sleep (10)
