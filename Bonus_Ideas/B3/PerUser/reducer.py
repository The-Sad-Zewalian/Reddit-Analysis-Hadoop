#!/usr/bin/python3

import sys

"""aggregates the results and then sorts them
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  

out=dict()
currentUser, count, Pos, Neg = sys.stdin.readline().strip().split("\t")
countSum = int(count)
PosSum = int(Pos)
NegSum = int(Neg)

for line in sys.stdin:
    user, count, Pos, Neg  = line.strip().split("\t")
    if user == currentUser:
        countSum += int(count)
        PosSum += int(Pos)
        NegSum += int(Neg)
    else:
        out[currentUser]=[countSum,PosSum,NegSum]
        currentSub = user
        countSum = int(count)
        PosSum = int(Pos)
        NegSum = int(Neg)

#sort dict the sort is base on the count of comments for the user
words_count = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

#display the top 50
top=50

for user, data in (words_count.items()):
    count=data[0]#Total number comments for the user
    Pos=data[1]#number of Positive comments
    Neg=data[2]#number of Negative comments
    Neu=count-Pos-Neg#number of Neutral comments
    if not top:
        break
    print("{}\t{:.2f}\t{:.2f}\t{:.2f}".format(user,(Pos/count)*100.0,(Neu/count)*100.0 ,(Neg/count)*100.0))
    top-=1