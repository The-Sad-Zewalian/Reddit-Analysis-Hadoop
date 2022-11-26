#!/usr/bin/python3

import sys
"""local combiner to decrease the work of reducer
Args:
    Standerd input line
Returns:
    Standerd output line 
"""

currentId, currentControversiality, Sum = sys.stdin.readline().strip().split("\t")
Sum=int(Sum)
for line in sys.stdin:
    id, controversiality, count = line.strip().split("\t")
    if id == currentId:
        Sum += int(count)
    else:
        print("{}\t{}\t{}".format(currentId,currentControversiality,Sum))
        currentId=id
        Sum=int(count)
        currentControversiality=controversiality