# Test for open a file.
tf = open("hamlet.txt", "rt" ,encoding="utf-8")
txt = tf.read()
txt = txt.split("\n")
print(len(txt))
#print(txt)
#while txt != "":
#    txt = tf.readline()
#    print(txt)
tf.close();