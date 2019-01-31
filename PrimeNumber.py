# Determine whether it is a prime number.
def decideNum(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def main():
    num = eval(input("输入一个数字: "))
    if decideNum(num):
        print("{} is a prime number!".format(num))
    else:
        print("{} is not a prime number!".format(num))


def main2():
    prnum = []
    for i in range(2, 10000, 1):
       if  decideNum(i):
           prnum.append(i)
    return prnum


result = main2()
#print(result)
for num in result:
    if num == result[-1]:
        print(num)
    else:
        print(num, end="、")