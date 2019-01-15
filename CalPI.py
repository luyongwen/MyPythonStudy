# This is a program for PI calculation.
def timetrans(t):
    hour = t // 3600
    minute = t % 3600 // 60
    second = t % 3600 % 60
    return hour, minute, second

import time
import random
inside = 0.0
N = 10000000
start = time.perf_counter()
for i in range(N):
    x = random.random()
    y = random.random()
    now = time.perf_counter()
    complete = (i + 1) / N
    if i % 1000 == 0:
        need = int((now - start) / complete - (now - start))
        h, m, s = timetrans(need)
    print("\r{:.2f}% {}h{}m{}s".format(complete * 100, h, m, s), end="")
    z = pow(x * x + y * y, 0.5)
    if z <= 1:
        inside += 1
end = time.perf_counter()
pi =  inside / N * 4
print("\n", pi)
print("The program spend {:.2f}s".format(end - start))
