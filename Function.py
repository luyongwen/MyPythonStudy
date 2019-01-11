def fact(n, m = 1):
    s = 1
    for i in range(1, n):
        s = s * i
    return s / m

a = fact(5, 6)
print(a)