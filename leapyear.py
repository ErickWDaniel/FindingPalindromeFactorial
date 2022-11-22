
leapYear = int(input("Enter Year to check if its Leap Year\n"))
if leapYear % 4 == 0  and leapYear % 100 == 0 and leapYear % 400 == 0:
    print(leapYear, "This is Leap year")
else:
    print(leapYear, "This in not a Leap year")
