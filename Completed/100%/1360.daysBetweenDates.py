# 1360. Number of Days Between Two Dates
# https://leetcode.com/problems/number-of-days-between-two-dates/description/
# Beats: 100.00%
def caluclate_days(date):
    output = 0
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    print(year, month, day)
    for i in range(1971, year):
        if i%4==0 and (i%100 !=0 or i%400==0):
            output += 366
        else:
            output += 365
    if year%4==0 and (year%100!=0 or year%400==0):
        days_in_month[1] = 29
    for j in range(month-1):
        output += days_in_month[j]
    output += day
    return output
def daysBetweenDates(date1, date2):
    date1 = date1.split("-")
    date2 = date2.split("-")
    day1 = caluclate_days(date1)
    # print(day1)
    day2 = caluclate_days(date2)
    # print(day2)
    return abs(day2 - day1)


date1 = "2019-06-29"
date2 = "2019-06-30"

date1 = "2020-01-15"
date2 = "2019-12-31"

date1 = "2009-08-18"
date2 = "2080-08-08"

date1 = "2100-09-22"
date2 = "1991-03-12"
print(daysBetweenDates(date1, date2))
