#!/usr/bin/python3

import sys


"""local combiner to decrease the work of reducer
Args:
    Standerd input line
Returns:
    Standerd output line 
"""

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
        print("{}\t{}\t{}\t{}".format(user,countSum,PosSum,NegSum))
        currentSub = user
        countSum = int(count)
        PosSum = int(Pos)
        NegSum = int(Neg)