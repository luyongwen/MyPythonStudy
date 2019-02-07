#!/usr/bin/env python3
#DayDayUpQ3
daybase = 1.0
dayfactor = eval(input("Enter a number:"))
for i in range(365):
    if i % 7 in [0, 6]:
        daybase = daybase * (1 - dayfactor)
    else:
        daybase = daybase * (1 + dayfactor)
print("Day result is {:.2f}".format(daybase))