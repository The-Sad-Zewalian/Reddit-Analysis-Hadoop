#!/usr/bin/python3

import sys

"""aggregates the results and then sorts them
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  

out=dict()
currentSub, count, Pos, Neg = sys.stdin.readline().strip().split("\t")
countSum = int(count)
PosSum = int(Pos)
NegSum = int(Neg)

for line in sys.stdin:
    Sub, count, Pos, Neg  = line.strip().split("\t")
    if Sub == currentSub:
        countSum += int(count)
        PosSum += int(Pos)
        NegSum += int(Neg)
    else:
        out[currentSub]=[countSum,PosSum,NegSum]
        currentSub = Sub
        countSum = int(count)
        PosSum = int(Pos)
        NegSum = int(Neg)

#sort dict the sort is base on the count of comments for the Sub
words_count = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

#display the top 50
top=50

for Sub, data in (words_count.items()):
    count=data[0]#Total number comments for the subreddit
    Pos=data[1]#number of Positive comments
    Neg=data[2]#number of Negative comments
    Neu=count-Pos-Neg#number of Neutral comments
    if not top:
        break
    print("{}\t{:.2f}\t{:.2f}\t{:.2f}".format(Sub,(Pos/count)*100.0,(Neu/count)*100.0 ,(Neg/count)*100.0))
    top-=1