#!/usr/bin/env python3
# Decide if it's a leap year.
def decideYear(year):
    if year % 400 == 0:
        return True
    if year % 100 != 0 & year % 4 == 0:
        return True
    else:
        return False


year = eval(input("请输入年份: "))
result = decideYear(year)
if result:
    print("{} is a leap year!".format(year))
else:
    print("{} is not a leap year!".format(year))
