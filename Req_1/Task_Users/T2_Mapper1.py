#!/usr/bin/python3

import json
import sys

"""maps the json object to a User, body, '1'
Args:
    json object
Returns:
    Standerd output line 
"""

#for line in sys.stdin:
#    User = line.split("\t")[0]
#    Body = line.split("\t")[1:-1]
#    Num = line.split("\t")[-1] 
#    print("{}\t{}\t{}".format(User,Body,Num))

for line in sys.stdin:
    try:
        Jobject = json.loads(line.encode('utf-8'))
        print("{}\t{}\t{}".format(Jobject['author'],Jobject['body'],'1'))
    except:
        None

