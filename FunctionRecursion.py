#!/usr/bin/env python3
# This is a test for function recursion.
def func(n):
    if n == 0:
        result = 1
    else:
        result = n * func(n - 1)
    return result


def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]


a = func(100)
print(a)
str1 = reverse("")
print(str1)