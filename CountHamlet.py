#!/usr/bin/env python3
# This is a program for count words in hamlet.
def getTxt():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in "~!@#$%^&*()_+{}|:<>?`-=[];',./":
        txt = txt.replace(ch, " ")
    return txt


def countWords(ls):
    count = dict()
    for word in ls:
        count[word] = count.get(word, 0) + 1
    return count

def tranTxt(str):
    str = str.split()
    return str


hamletTxt = getTxt()
dic = countWords(tranTxt(getTxt()))
item = list(dic.items())
item.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = item[i]
    print("{}:{}".format(word, count), end="    ")
