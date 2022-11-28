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
counter = 0
for line in sys.stdin:
  Subreddit = line.split("\t")[0]
  Body = line.split("\t")[1:-1]
  if len(Body) >0:
     if Subreddit in Dict1:
        Dict1[Subreddit] += 1
        Dict2[Subreddit].append(Body)
     else:
        Dict1[Subreddit] = 1
        Dict2[Subreddit] = [Body]
Sorted = sorted(Dict1.items(), key=lambda x:x[1], reverse = True)
for i in range(len(Sorted)):
    List = Dict2[Sorted[i][0]]
    for j in range(len(List)):
        print("{}\t{}\t{}".format(Sorted[i][0],List[j][0],'1'))
