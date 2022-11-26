#!/usr/bin/python3

import sys

"""aggregates the results and then sort them
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  
edited_commentsSum, deleted_commentSum, deleted_usersSum = sys.stdin.readline().strip().split("\t")
edited_commentsSum=int(edited_commentsSum)
deleted_commentSum=int(deleted_commentSum)
deleted_usersSum=int(deleted_usersSum)
for line in sys.stdin:
    edited, deleted_comment, deleted_user = line.strip().split("\t")
    edited_commentsSum+=int(edited)
    deleted_commentSum+=int(deleted_comment)
    deleted_usersSum+=int(deleted_user)

print("{}\t{}\t{}".format(edited_commentsSum, deleted_commentSum, deleted_usersSum))

