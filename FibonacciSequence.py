#!/usr/bin/env python3
# This is a fuction to calculate Fibonacci sequence.
def Fibonacci_sequence(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci_sequence(n - 1) + Fibonacci_sequence(n - 2)


a = Fibonacci_sequence(40)
print(a)
