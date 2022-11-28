#!/usr/bin/python3

import sys


"""local combiner to decrease the work of reducer
Args:
    Standerd input line
Returns:
    Standerd output line 
"""

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
        print("{}\t{}\t{}\t{}".format(currentSub,countSum,PosSum,NegSum))
        currentSub = Sub
        countSum = int(count)
        PosSum = int(Pos)
        NegSum = int(Neg)