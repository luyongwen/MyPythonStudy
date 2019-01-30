# Test for open a file.
tf = open("f.txt", "rt" ,encoding="utf-8")
txt = tf.read(2)
while txt != "":
    txt = tf.read(2)
    print(txt)
tf.close();