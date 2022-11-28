#!/usr/bin/python3

import json
import sys

"""maps the json object to a subbreddit, body, '1'
Args:
    json object
Returns:
    Standerd output line 
"""

#for line in sys.stdin:
#    Subreddit = line.split("\t")[0]
#    Body = line.split("\t")[1:-1]
#    Num = line.split("\t")[-1] 
#    print("{}\t{}\t{}".format(Subreddit,Body,Num))

for line in sys.stdin:
    try:
        Jobject = json.loads(line.encode('utf-8'))
        print("{}\t{}\t{}".format(Jobject['subreddit'],Jobject['body'],'1'))
    except:
        None

