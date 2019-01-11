# This is a program for PI calculation.
import time
import random
inside = 0.0
N = 10000000
start = time.perf_counter()
for i in range(N):
    x = random.random()
    y = random.random()
    z = pow(x * x + y * y, 0.5)
    if z <= 1:
        inside += 1
end = time.perf_counter()
pi =  inside / N * 4
print(pi)
print("The program spend {}s".format(end - start))