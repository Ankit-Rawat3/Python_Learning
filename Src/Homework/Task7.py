#Leap Year Checker:


year=int(input("Enter any Year  : \n"))

if (year % 4 == 0) and (year % 100 != 0) or(year % 400 == 0):
    print(f"This {year} is a Leap year")
else:
    print(f"This {year} is not a Leap year")

    