#!/usr/bin/python3

import sys

"""Counting all topics -> So finally we could print the most frequent topics 
Args:
    (subbreddit, Topic, '1')
Returns:
    subbreddit, Topic, count
"""

Dict1 = {}
for line in sys.stdin:
    Subreddit, Topic, Num = line.split("\t")
    if ("{}\t{}".format(Subreddit,Topic)) in Dict1:
        Dict1["{}\t{}".format(Subreddit,Topic)] += 1
    else:
        Dict1["{}\t{}".format(Subreddit,Topic)] = 1

for key, value in Dict1.items():
    print("{}\t{}\t{}".format(key.split("\t")[0],key.split("\t")[1],value))
