≈çy#!/bin/bash

batteryLevel=`pmset -g batt | grep "%" | awk '{print $2}' | tr -d ';'`

python /Users/Anshu/Documents/Personal/Scripts/greetMe.py ${batteryLevel}