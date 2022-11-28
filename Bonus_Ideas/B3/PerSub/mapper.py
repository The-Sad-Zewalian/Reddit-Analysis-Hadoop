#!/usr/bin/python3

import sys
import json


"""maps the json object to a subreddit, intial count(1), and two numbers that are either one or zero
output is subreddit, 1, pos_flag , neg_flag 
Args:
    json object
Returns:
    Standerd output line 
"""

for line in sys.stdin:
    try:
        Jobject=json.loads(line.encode('utf-8'))
        print("{}\t{}\t{}\t{}".format(Jobject['subreddit'],1,int(Jobject['score']>0),int(Jobject['score']<0)))
    except:
        continue


