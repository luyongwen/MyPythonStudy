# This is a resolve for hannoi.
count = 0


def hanoi(n, a, b, c):
    global count
    if n == 1:
        count += 1
        print(count, ":", str(a), '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(count, ":", a, '-->', c)
        count += 1
        hanoi(n - 1, b, a, c)


print(hanoi(3, 1, 2, 3))
print(count)
