#!/usr/bin/env python3
#DayDayUpQ4
import time
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup

dayfactor = 0.01
start = time.time()
while dayup(dayfactor) < 37.78:
    dayfactor = dayfactor + 0.001
end = time.time()
print("Dayfactor is {:.3f}, The program spend {:.4f}s".format(dayfactor, end - start))