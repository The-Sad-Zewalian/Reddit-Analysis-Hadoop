#!/usr/bin/python3

import sys

"""Sorting all subreddits to be in descending way that makes top subreddits at first
Args:
    Standerd input line (subreddit, body, '1')
Returns:
    Standerd output line 
"""  

Dict1 = {}  # Just to sort with
Dict2 = {}  # Like temp
for line in sys.stdin:
  User = line.split("\t")[0]
  Body = line.split("\t")[1:-1]
  if len(Body) >0:
     if User in Dict1:
        Dict1[User] += 1
        Dict2[User].append(Body)
     else:
        Dict1[User] = 1
        Dict2[User] = [Body]

Sorted = sorted(Dict1.items(), key=lambda x:x[1], reverse = True)

for i in range(len(Sorted)):
    List = Dict2[Sorted[i][0]]
    for j in range(len(List)):
        print("{}\t{}\t{}".format(Sorted[i][0],List[j][0],'1'))

