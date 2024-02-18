validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day =  int(input("Enter the day: "))
if int(year) <= MIN_YEAR: 
 validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: 
 validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: 
 validDate = False
if validDate is True:
    print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date")
else:
    print(str(month) + "/" + str(day) + "/" + str(year) + " is an invalid date")