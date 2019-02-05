# This is a program for test wordcloud.
import jieba
import wordcloud
import scipy.misc
mask = scipy.misc.imread("3170207056岳竹霖.jpg")
string = open("三国.txt", "rt", encoding="utf-8").read()
ls = jieba.lcut(string)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", background_color="white", mask=mask)
w.generate(txt)
w.to_file("C:\\Users\\LYW\\Pictures\\hamlet.gif")