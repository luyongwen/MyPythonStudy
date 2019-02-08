#!/usr/bin/env python3
tf = open("primenum.txt", "rt+")
string = tf.read()
print(string)
string.replace(" ", "、")
print(string)
