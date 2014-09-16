#!/usr/bin/python

import sys
import re

def run_reduce():
    
    result = []
    order_list = []
    lineitem_list = []

    oldkey = None
        
    for line in sys.stdin:
        data = line.split("\t")
        
        if len(data) != 2:
            continue

        newkey, records = data
        r = records.replace("[", "").replace("'", "")
        records = re.split("], ", r)
        
        if oldkey and oldkey != newkey:
            if order_list:
                for o in order_list:
                    o = o.replace("]", "").strip('\n')

                    for l in lineitem_list:
                        l = l.replace("]", "").strip('\n')
                        lineitem_attr = []
                        lineitem_attr = l.split(", ")
                        lineitem_attr = lineitem_attr[2:]
                        result.append(o + ", " + ', '.join(lineitem_attr))
            
            order_list = []
            lineitem_list = []
        
        oldkey = newkey
            
        for r in records:
            if "order" in r:
                order_list.append(r)
            elif "line_item" in r:
                lineitem_list.append(r)
    
    if oldkey != None:     
        if order_list:
                for o in order_list:
                    o = o.replace("]", "").strip('\n')
                    for l in lineitem_list:
                        l = l.replace("]", "").strip('\n')
                        lineitem_attr = []
                        lineitem_attr = l.split(", ")
                        lineitem_attr = lineitem_attr[2:]
                        result.append(o + ", " + ', '.join(lineitem_attr))

    for i in result:
        print i             
            
def main():
    run_reduce()

if __name__ == "__main__":
    main()

