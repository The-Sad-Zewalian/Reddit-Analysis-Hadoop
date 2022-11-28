#!/usr/bin/python3

import sys

"""Sorting all topics per User, and we already have all Users sorted 
Args:
    (User, Topic, count)
Returns:
    User
    Topic1, count
    Topic2, count
"""

Dict_User_Topics = {}
for line in sys.stdin:
  User, Topic,value = line.split("\t")
  if User in Dict_User_Topics:
    Dict_User_Topics[User][Topic] = value
  else:
    Dict_User_Topics[User] = {}
    Dict_User_Topics[User][Topic] = value

for key1, value1 in Dict_User_Topics.items():
  Dict_User_Topics[key1] = sorted(value1.items(), key=lambda x:x[1], reverse = True)[0:min(10,len(value1.items()))]
  print()
  print("User: {}".format(key1))
  print()
  for i in range(len(Dict_User_Topics[key1])):
    print("{}\t{}".format(Dict_User_Topics[key1][i][0],Dict_User_Topics[key1][i][1]))