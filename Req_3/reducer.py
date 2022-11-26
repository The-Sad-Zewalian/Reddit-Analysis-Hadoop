#!/usr/bin/python3

import sys

"""aggregates the results and then sort them
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  

#intiate our starting counts
currentWord, ups, downs = sys.stdin.readline().strip().split("\t")
upSum=int(ups)
downSum=int(downs)
out=dict()

for line in sys.stdin:

    word, ups, downs = line.strip().split("\t")

    if word == currentWord:#if we are still counting for the same word
        upSum += int(ups)
        downSum += int(downs)
    else:
        out[word]=[upSum,downSum]
        currentWord=word
        upSum=int(ups)
        downSum=int(downs)

#sort dict
words_count = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

top=1000
for word, votes in words_count.items():
    if(not top):
        break
    print("{}\t{}\t{}".format(word,votes[0],votes[1]))
    top-=1