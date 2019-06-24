#!/usr/bin/python
#
# Program : audacity-label-changer.py
# Version : 1.3
# Use : 
# Makes files from an existing labelfile (containing points).
# Converts this into tracks for use in audacity.
# Also makes a conversion into tracks in hh:mm:ss format,
# for FFmpeg program based splitting.

# Make sure you have installed the desired python-modules.
# How to run :
# Make the program executable, dubbleclick and choose open in terminal.
# (make it executable : right click -> rights -> execute or  chmod +x "filname")
# You can run it also directly from the terminal with : python audacity-label-changer.py
# Or run it from the terminal with : ./audacity-label-changer.py
#
# Author : Folkert van der Meulen
# Date   : 24/06/2019
#
# Copyright 2019 Folkert van der Meulen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------


import Tkinter as tk
import tkFileDialog
import datetime
import time
import os

#clear terminal screen
os.system('clear')

# info before starting
print "audacity-label-changer version 1.3"
print "\n"
print "Makes files from an existing labelfile (containing points)." 
print "Converts this into tracks for use in audacity."
print "Also makes a conversion into tracks in hh:mm:ss format,"
print "for FFmpeg program based splitting."
print "\n"
print "  for a good calculation, audacity labelfile"
print "     has to have a first and a last point"
print "in example below, this is => 1=first and 8=last"
print "    ( startime and stoptime are the same )"
print "     |---------example-audiofile--------|"
print "     |     |    |     |   |    |    |   |"
print "     1     2    3     4   5    6    7   8"
print "            labeltime in seconds         "
print "\n"

# get labelfile for use in commandline
root = tk.Tk()
root.withdraw()
labelfile = tkFileDialog.askopenfilename(initialdir = '~/Desktop/mijn_sh_scripts/YTdl-bash/NA-bak/split en labels test - Technotronic - Trip On This - Remix Album_backup', filetypes=[('Supported types',('.txt'))], title='Load audacity label point file')
print labelfile

print "\n"

#read textfile lines and convert "label dots in seconds"  to "hh:mm:ss track format"
lines = [line.rstrip('\n') for line in open ('%s'%(labelfile))]

# make empty text file for tracks in seconds 
# for connecting labelpoints 1 to 2, 2 to 3, etc for use in audacity
# |------------audiofile-------------|
# |<--->|<-->|<--->|<->|<-->|<-->|<->|
# 1     2    3     4   5    6    7   8
#        labeltime in seconds
labeltracks = open("labels_for_audacity.txt","w+")

# make empty text file for tracks in hh:mm:ss format
# for connecting labelpoints 1 to 2, 2 to 3, etc for use in audiosplit.py (makes use of ffmpeg)
# |------------audiofile-------------|
# |<--->|<-->|<--->|<->|<-->|<-->|<->|
# 1     2    3     4   5    6    7   8
#        labeltime in hh:mm:ss
labeltrackshhmmss = open("labels_for_audiosplit.txt","w+")

#print lines

#define lists
starttime = []
stoptime = []
tracknumber = []
starttimehhmmss = []
stoptimehhmmss = []

print "Representation of the original audacity file    :"
print "-------------------------------------------------"
print "     |---------example-audiofile--------|"
print "     |     |    |     |   |    |    |   |"
print "     1     2    3     4   5    6    7   8"
print "            labeltime in seconds         "
print "-------------------------------------------------"

for values in lines:
   print values
   values = values.replace(",", ".")
   starttime+= [starttime.append(values.split("\t", values.count("\t"))[0])]
   stoptime+= [stoptime.append(values.split("\t", values.count("\t"))[1])]
   tracknumber+= [tracknumber.append(values.split("\t", values.count("\t"))[2])]

print "-------------------------------------------------"
print "\n"

#remove 'None' values
#https://www.geeksforgeeks.org/python-remove-none-values-from-list/
starttime = list(filter(None, starttime)) 
stoptime = list(filter(None, stoptime)) 
tracknumber = list(filter(None, tracknumber)) 

print "Representation of the changed file for audacity :"
print "  (labelpoints 1 to 2, 2 to 3, etc connected)"
print "-------------------------------------------------"
print "     |---------example-audiofile--------|"
print "     |<--->|<-->|<--->|<->|<-->|<-->|<->|"
print "     1     2    3     4   5    6    7   8"
print "            labeltime in seconds         "
print "-------------------------------------------------"

#make a new sublist tracknumberlabels with 1 number less
#for connecting labelpoints 1 to 2, 2 to 3, etc for use in audacity
#make a new file for use in audacity
tracknumberlabels = tracknumber[:-1]
for index, item in enumerate(tracknumberlabels):
    #print starttime[index] + "\t" + stoptime[index+1] + "\t" + tracknumberlabels[index]
    audacitytrackformat = starttime[index] + "\t" + stoptime[index+1] + "\t" + tracknumberlabels[index]
    audacitytrackformat = audacitytrackformat.replace(".", ",")
    print audacitytrackformat
    labeltracks.write(audacitytrackformat + "\n")

print "-------------------------------------------------"
print "\n"

#make all values in starttime floats (for conversion from seconds to hhmmss)
#https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
#was a tricky part, but added "starttimehhmmss+" line with "[index]" as above "for values in lines"
#the lists starttimehhmmss stoptimehhmmss have to be filled with values first
#this was the solution!
#has to be (starttime) in "for index, item in enumerate(starttime)" otherwise it won't work
for index, item in enumerate(starttime):
    starttime[index] = float(item)
    starttimehhmmss+= [str(datetime.timedelta(seconds=round(starttime[index])))]
    stoptime[index] = float(item)
    stoptimehhmmss+= [str(datetime.timedelta(seconds=round(stoptime[index])))]
    #this printformat is for checking only
    #print starttimehhmmss[index] + "\t" + stoptimehhmmss[index] + "\t" + tracknumber[index] 

print "Representation of the changed file for audacity :"
print "  (labelpoints 1 to 2, 2 to 3, etc connected)"
print "-------------------------------------------------"
print "     |<--->|<-->|<--->|<->|<-->|<-->|<->|"
print "     1     2    3     4   5    6    7   8"
print "        labeltime in hh:mm:ss format     "
print "-------------------------------------------------"

#stoptimehhmmss[index+1] will not work in earlier for loop because it is 1 step ahead (not all the list have been filled then)
for index, item in enumerate(tracknumberlabels):
    #above lists will be used to connect labelpoint 1 to 2, 2 to 3, etc in hhmmss format
    #this format can be used for splitting audio files with split.py (without re-encoding)
    print starttimehhmmss[index] + "\t" + stoptimehhmmss[index+1] + "\t" + tracknumberlabels[index]
    labeltrackshhmmss.write(starttimehhmmss[index] + "\t" + stoptimehhmmss[index+1] + "\t" + tracknumberlabels[index]  + "\n")    

print "-------------------------------------------------"  
print "\n"

# Close open files
labeltracks.close()
labeltrackshhmmss.close()

print "New files have been saved in the program directory !"
print "\n"

#read variable exit, after input the program stops 
exit = raw_input("enter to exit :")