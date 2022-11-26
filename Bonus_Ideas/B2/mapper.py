#!/usr/bin/python3

import sys
import json


"""maps the json object to:
first:  indicates whether the comment was edited or not
second: indicates if the body is deleted or not
third:  indicates if the user was deleted or not
Args:
    json object
Returns:
    Standerd output line 
"""
    #

for line in sys.stdin:
    try:
        Jobject=json.loads(line.encode('utf-8'))
        print("{}\t{}\t{}".format(1*(Jobject["edited"]!=False), 1*(Jobject['author']=='[deleted]'), 1*(Jobject['body']=='[deleted]')))
    except:
        continue


