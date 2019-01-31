# Determine whether it is a prime number.
def decideNum(num):
    for i in range(1, int(num / 2)):
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
    for i in range(2, 100, 1):
       if  decideNum(i):
           print(i)


main2()