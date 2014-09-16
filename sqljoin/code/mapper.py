#!/usr/bin/python

import sys
import json
import re

def run_map():
    
    records = {}
    
    for line in sys.stdin:
        in_data = line.strip().split(",")
        key = in_data[1].replace('"', '').strip()
        records.setdefault(key, [])
        records[key].append(line.strip())
               
    for k, v in records.items():
        print "{0}\t{1}".format(k, v)

def main():
    run_map()

if __name__ == "__main__":
    main()
    