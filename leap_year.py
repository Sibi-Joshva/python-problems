def leap_year(year):
   
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
    
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{} is a leap year".format(year))

    else:
        print("{} is not a leap year ".format(year))


year = int(input("Enter the year : "))
leap_year(year)
