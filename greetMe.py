import os
import random
import sys
from datetime import datetime
import time

user = "Anshu"
currentTime = str(datetime.now().time())
battery = sys.argv[1]
stringHour = currentTime[0:2]
intHour = int(stringHour)
minute = currentTime[3:5]
day = "AM"

if stringHour == "00": stringHour = "midnight"
if stringHour == "12": 
    stringHour = "noon"
    day = "PM"

if intHour > 12:
    intHour = intHour - 12
    day = "PM"
    stringHour = str(intHour)

theTime = stringHour + ":" + minute + " " +  day

greeting = "Good Morning"

#if intHour >= 6 and day == "AM":
   #greeting = "Good Morning"
if intHour <= 4 and day == "PM":
    greeting = "Good Afternoon"
elif intHour >= 5 and day == "PM":
    greeting = "Good Evening"
elif intHour >= 9 and day == "PM":
    greeting = "Good Night"

os.system("say " + greeting + user)
os.system("say It is " + theTime)
time.sleep(1)
os.system("say " + battery + " battery remaining")
print battery
