#!/usr/bin/python3

import sys

"""aggregates the results and then sort them
Args:
    Standerd input line
Returns:
    Standerd output line 
"""  
currentId, currentControversiality, edited_commentsSum, deleted_commentSum, deleted_usersSum = sys.stdin.readline().strip().split("\t")
edited_commentsSum=int(edited_commentsSum)
deleted_commentSum=int(deleted_commentSum)
deleted_usersSum=int(deleted_usersSum)
out=dict()
for line in sys.stdin:
    id, controversiality, edited, deleted_comment, deleted_user = line.strip().split("\t")
    if id == currentId:
        edited_commentsSum+=int(edited)
        deleted_commentSum+=int(deleted_comment)
        deleted_usersSum+=int(deleted_user)
    else:
        #print("{}\t{}\t{}\t{}\t{}".format(currentId,currentControversiality, edited_commentsSum, deleted_commentSum, deleted_usersSum))
        out[currentId]=[currentControversiality,edited_commentsSum, deleted_commentSum, deleted_usersSum]
        currentId=id
        edited_commentsSum=int(edited)
        deleted_commentSum=int(deleted_comment)
        deleted_usersSum=int(deleted_user)
        currentControversiality=controversiality

#sort dict
words_count = dict(sorted(out.items(), key=lambda item: item[1], reverse=True))

#display the top 1000
top=1000
for word, votes in words_count.items():
    if not top:
        break
    print("{}\t{}\t{}\t{}\t{}".format(word,votes[0],votes[1],votes[2],votes[3]))
    top-=1