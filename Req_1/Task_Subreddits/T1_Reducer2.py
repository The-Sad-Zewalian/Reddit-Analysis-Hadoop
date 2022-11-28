#!/usr/bin/python3

import sys

"""Sorting all topics per subreddit, and we already have all subreddits sorted 
Args:
    (subbreddit, Topic, count)
Returns:
    subbreddit
    Topic1, count
    Topic2, count
"""

Dict_Sub_Topics = {}
for line in sys.stdin:
  Subreddit, Topic,value = line.split("\t")
  if Subreddit in Dict_Sub_Topics:
    Dict_Sub_Topics[Subreddit][Topic] = value
  else:
    Dict_Sub_Topics[Subreddit] = {}
    Dict_Sub_Topics[Subreddit][Topic] = value
for key1, value1 in Dict_Sub_Topics.items():
  Dict_Sub_Topics[key1] = sorted(value1.items(), key=lambda x:x[1], reverse = True)[0:min(10,len(value1.items()))]
  print()
  print("Subreddit: {}".format(key1))
  print()
  for i in range(len(Dict_Sub_Topics[key1])):
    print("{}\t{}".format(Dict_Sub_Topics[key1][i][0],Dict_Sub_Topics[key1][i][1]))
