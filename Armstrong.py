# Calculate Armstrong number.
# 判断是否为阿姆斯特朗数返回Ture或False
def decArm(num):
    n = decNum(num)
    s = 0
    strnum = str(num)
    for c in strnum:
        s = s + pow(int(c), n)
    if s == num:
        return True
    else:
        return False


# 判断是几位数
def decNum(num):
    n = 1
    while num // pow(10, n) != 0:
        n += 1
    return n


for i in range(1, 1000):
    result = decArm(i)
    if result:
        print(i)