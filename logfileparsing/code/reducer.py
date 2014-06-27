#!/usr/bin/python

import sys

oldkey = None
pagecount = 0
   
# Loop around the data
# It will be in the format key\tval
# Where key is the webpage name, val is the visit count
#
# All the visits for a particular web page will be counted.
   
for line in sys.stdin:
    data = line.split("\t")
        
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
        
    thiskey, count = data
        
    if oldkey and oldkey != thiskey:
        print oldkey, "\t", pagecount
        pagecount = 0
        
    oldkey = thiskey
    pagecount += int(count) 

if oldkey != None:
    print oldkey, "\t", pagecount

