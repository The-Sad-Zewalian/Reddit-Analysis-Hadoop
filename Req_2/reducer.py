#!/usr/bin/python3

import sys

"""aggregates the results, sort them and finally prints the results
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  

currentId, currentControversiality, Sum = sys.stdin.readline().strip().split("\t")
Sum=int(Sum)
out=dict()
for line in sys.stdin:
    id, controversiality, count = line.strip().split("\t")
    if id == currentId:
        Sum += int(count)
    else:
        out[currentId]=[currentControversiality,Sum]
        currentId=id
        Sum=int(count)
        currentControversiality=controversiality

#sort dict
words_count = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

#print output
for ID, data in words_count.items():
    print("{}\t{}\t{}".format(ID, data[0], data[1]))