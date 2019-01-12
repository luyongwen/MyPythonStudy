# This is a test for time.
import time
date = time.gmtime()
strdate = time.strftime("%a %b %d %H:%M:%S %Y", date)
print(strdate)
print(date)
print(time.ctime())