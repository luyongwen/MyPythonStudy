#DayDayUpQ2
dayfactor = 0.005
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("Dayup:{:.2f}\tDaydown:{:.2f}".format(dayup, daydown))