# Test for time.
import time
result = 0
start = time.time()
for i in range(1000000):
    result = i + result
end = time.time()
print(start - end, '\nresult is', result)
time.strftime
