#!/usr/bin/python3

import sys


"""local combiner to decrease the work of reducer
Args:
    Standerd input line
Returns:
    Standerd output line 
"""
currentId, currentControversiality, edited_commentsSum, deleted_commentSum, deleted_usersSum = sys.stdin.readline().strip().split("\t")
edited_commentsSum=int(edited_commentsSum)
deleted_commentSum=int(deleted_commentSum)
deleted_usersSum=int(deleted_usersSum)
for line in sys.stdin:
    id, controversiality, edited, deleted_comment, deleted_user = line.strip().split("\t")
    if id == currentId:
        edited_commentsSum+=int(edited)
        deleted_commentSum+=int(deleted_comment)
        deleted_usersSum+=int(deleted_user)
    else:
        print("{}\t{}\t{}\t{}\t{}".format(currentId,currentControversiality, edited_commentsSum, deleted_commentSum, deleted_usersSum))
        currentId=id
        edited_commentsSum=int(edited)
        deleted_commentSum=int(deleted_comment)
        deleted_usersSum=int(deleted_user)
        currentControversiality=controversiality
        