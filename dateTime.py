import datetime

def printTimes():
    print('\n',"Current date and time is: ",datetime.datetime.now(),'\n')
    print("The time is: ",datetime.datetime.now().time())


# def dateDif():
y1,m1,d1 = input("Enter the YEAR: "), input("Enter the MONTH: "), input("Enter the DAY: ")
date1 = datetime.date(int(y1),int(m1),int(d1))
print("The first date is: ",date1)

y2,m2,d2 = input("Enter the YEAR: "), input("Enter the MONTH: "), input("Enter the DAY: ")
date2 = datetime.date(int(y2),int(m2),int(d2))
print("The second date is: ", date2)

#Number of dates between the two provided:
deltaDays = abs(date1 - date2)
print(deltaDays)

print("Number of days gap is: ", deltaDays, "\n")
if date1 > date2:
    print("Date 1 is larger")
if date1 < date2:
    print("Date 2 is larger")
else:
    print("These are the same dates")
