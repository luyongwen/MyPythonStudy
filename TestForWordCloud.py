#!/usr/bin/env python3
# This is a program for test wordcloud.
import jieba
import wordcloud
import scipy.misc
file_name = "wujiaoxing.jpg"
mask = scipy.misc.imread(file_name)
string = open("三国.txt", "rt", encoding="utf-8").read()
ls = jieba.lcut(string)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", background_color="white", mask=mask)
w.generate(txt)
w.to_file("/Users/LYW/Pictures/" + file_name)