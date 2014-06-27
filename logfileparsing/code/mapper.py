#!/usr/bin/python

import sys

for line in sys.stdin:
    if not ".php" in line:
        continue
    else:    
        webpage = line.split('[')[1].split(']')[1].split('?')[0].split('/')[1]
        
        if ".php" in webpage:
            pageparts = webpage.split()
            if len(pageparts) == 1 and pageparts[0].endswith(".php") and pageparts[0][0].isalpha():
                print "{0}\t{1}".format(webpage, 1)
