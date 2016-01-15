## procedure isALeapYear takes a year and returns True is it is a leap year
## and false if it is not

def isALeapYear(year):
    if year % 4 != 0:
        isLeap = False
    else:
        if year % 100 != 0:
            isLeap = True
        else:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
    return isLeap

## Test is LeapYear
# year = 1900

# for year in range(1800, 2016):
#    print 'The year ' + str(year) + ' is a ' + isLeap(year) + ' year'

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##

    ## days for each month for both leap years and non leap years
    notleap = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    leap = 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    ## for cases where the dates entered are of the same year
    if year2 == year1:
        ## for cases where dates are same year and same month
        if month2 == month1:
            days = day2 - day1
        ## for cases dates are same year but different months
        else:
            ## find if it is a leap year
            if isALeapYear(year1) == True:
                daysOfMonth = leap
            else:
                daysOfMonth = notleap

            ## add rest of days of 1st month
            days = daysOfMonth[month1 - 1] - day1

            ## add days for months in between
            for i in range(month1 + 1, month2):
                days = days + daysOfMonth[i - 1]

            ## add days for last month
            days = days + day2

    ## for cases where years are different
    else:
        ## find if it is a leap year
        if isALeapYear(year1) == True:
            daysOfMonth = leap
        else:
            daysOfMonth = notleap

        ## add rest of days of 1st month
        days = daysOfMonth[month1 - 1] - day1

        ## add days for months until end of starting year
        for i in range(month1 + 1, 13):
            days = days + daysOfMonth[i - 1]

        ## add days of all years in between starting and fin year
        for i in range(year1 + 1, year2):
            if isALeapYear(i) == True:
                days = days + 366
            else:
                days = days + 365

        ## add days in the finishing year upto the final day
        if isALeapYear(year2) == True:
            daysOfMonth = leap
        else:
            daysOfMonth = notleap

        for i in range(1, month2):
            days = days + daysOfMonth[i - 1]

        days = days + day2

    return days

print daysBetweenDates(1983,3,19,2015,12,28)
