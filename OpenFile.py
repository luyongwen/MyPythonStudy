# Test for open a file.
tf = open("f.txt", "rt" ,encoding="utf-8")
print(tf.read())
tf.close();