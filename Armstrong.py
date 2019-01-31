# Calculate Armstrong number.
def decArm(num):
    n = decNum(num)
    s = 0
    strnum = str(num)
    for c in strnum:
        s = s + int(c)
    if s == num:
        return True
    else:
        return False


def decNum(num):
    n = 1
    while num // pow(10, n) != 0:
        n += 1
    return n


for i in range(1, 1000):
    result = decArm(i)
    if result:
        print(i)