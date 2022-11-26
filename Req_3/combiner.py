#!/usr/bin/python3

import sys

"""local combiner to decrease the work of reducer
Args:
    Standerd input line
Returns:
    Standerd output line 
"""

#intiate our starting counts
currentWord, ups, downs = sys.stdin.readline().strip().split("\t")
upSum=int(ups)
downSum=int(downs)

for line in sys.stdin:
    word, ups, downs = line.strip().split("\t")
    #if we are still counting for the same word
    if word == currentWord:
        upSum += int(ups)
        downSum += int(downs)
    #then we are counting for a new word
    else:
        print("{}\t{}\t{}".format(word,upSum,downSum))
        currentWord=word
        upSum=int(ups)
        downSum=int(downs)

