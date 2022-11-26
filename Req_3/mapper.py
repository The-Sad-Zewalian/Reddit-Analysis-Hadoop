#!/usr/bin/python3

import sys
import json
from string import digits
import re

remove_digits  = str.maketrans('', '', digits)#to remove digits from the text

#Our Long List Of Stop Words
stop_words = [
'#', '$', '%', '&', "''", "'ll", "'m", "'s", "'ve", '(', ')', '*', '+', ',', '-', '.', ':', ';', '=', '?', '@','!','~', '[', ']', '_','``','\'re','/s','\'','\"', '–','’',
'a', 'about', 'above', 'after', 'again', 'against','ain', 'all', 'already','always', 'also', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at',
'b', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by','best','become',
'c', 'can', 'couldn',"couldn't", 
'd', 'deleted', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'dont', 'down','during','deleted', 
'e', 'each', 'even','early','enough','else','etc','every',
'f', 'few', 'for', 'from', 'further',
'g', 'good', 'great', 
'h', 'had','hadn',"hadn't", 'has', 'hasn', "hasn't",'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself','him', 'himself', 'his', 'how','haha','https','however','hey','http',
'i', 'if', 'im', 'in', 'into','is', 'isn', "isn't", 'it', "it's", 'its', 'itself',
'j', 'just',
'k', 'known',
'l', 'like', 'll', 'long','lot', 'lt','ly','let','lol',
'm', 'ma', 'me', 'mightn', "mightn't", 'more','most', 'much', 'mustn', "mustn't", 'my', 'myself', 'maybe',
'n', "n't", 'near', 'needn', "needn't", 'new', 'no', 'nor', 'not', 'now', 'nye','na','name','never',
'o', 'of', 'off', 'on', 'once', 'one', 'only', 'or','other', 'our', 'ours', 'ourselves', 'out', 'over', 'own','oh',
'p', 'please',
'q',
'r', 're',
's', 'same','say','shan', "shan't",'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some','such','shortly','sure','something','someone','sorry',
't', 'than', 'that', "that'll", 'thats', 'the', 'their', 'theirs', 'them', 'themselves','then', 'there', 'these','they', 'this','those','though','through','to','too','tell','talk', 
'u', 'under','until','up','upon','us','use',
'v', 've','very','vw',
'w', 'was','wasn', "wasn't",'we','were','weren',"weren't",'what','when','where','which','while','who','whom','why','will','wish','with','won',"won't",'would', 'wouldn',"wouldn't",'wo', 
'x',
'y', 'ya','yes','you',"you'd","you'll","you're","you've",'your','yours','yourself','yourselves','yea','yeah','year',
'z'
]
stop_words=set(stop_words)

def ProcessBody(text):
    """this function performs the following operations on the given text to obtain unique word
    1- turn text to lowercase and tokenize it
    2- remove all digits
    3- remove stopwords
    4- return a set of unique words
    Args:
        text (str)
    Returns:
        topics (set) 
    """
    #Remove Emojis and other weird chars
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                              "]+", flags=re.UNICODE)


    text = emoji_pattern.sub(r'', text)
    text = text.replace('.',' ').replace('-',' ').replace('_',' ').replace('/',' ').replace('\\',' ').replace(']',' ').replace('$',' ')
    text = text.replace(',',' ').replace('\'',' ').replace('<',' ').replace('>',' ').replace('~',' ').replace('[',' ').replace('&',' ')
    text = text.replace('+',' ').replace('=',' ').replace(':',' ').replace('^',' ').replace('!',' ').replace('?',' ').replace('\n',' ')
    text = text.replace('|',' ').replace('(',' ').replace(')',' ').replace('{',' ').replace('}',' ').replace('"',' ').replace('*',' ')
    text = text.replace('\t'," ")
    
    text_tokens = text.lower().split(" ")#turned text to lowercase then split it into words 
    tokens_without_sw = [word.translate(remove_digits) for word in text_tokens ]#remove digits
    tokens_without_sw = [word for word in tokens_without_sw if not word in stop_words]#remove stop words
    tokens_without_sw = [word for word in tokens_without_sw if  not word.endswith('ly')] #remove words with 'ly' suffix
    tokens_without_sw = [word for word in tokens_without_sw if  not word.endswith('ing')]#remove words with 'ing' suffix
    tokens_without_sw = [word for word in tokens_without_sw if  not word.endswith('ful')]#remove words with 'ful' suffix
    tokens_without_sw = [word for word in tokens_without_sw if  not word.endswith('ed')]#remove words with 'ed' suffix
    Tokens = [word for word in tokens_without_sw if  not word.endswith('ous')]#remove words with 'ous' suffix
    Tokens = [word for word in tokens_without_sw if word!=" "]
    Tokens=filter(lambda word: len(word) >3 and len(word) <= 15, Tokens)#filter on length of token to remove very long tokens
    return set(Tokens)



"""maps the json object to a word and its intial upvotes and downvotes
Args:
    json object
Returns:
    Standerd output line 
"""

for line in sys.stdin:
    try:
        Jobject=json.loads(line.encode('utf-8'))
        for word in ProcessBody(Jobject['body']):
            if len(word)!=0:
                print("{}\t{}\t{}".format(word,Jobject['ups'],Jobject['downs']))
    except:
        None