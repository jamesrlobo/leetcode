# 1154. Day of the Year
# https://leetcode.com/problems/day-of-the-year/description/
# Beats: 83.76%
def dayOfYear(date):
    dates = date.split("-")
    months = {0:0,
              1:31,
              2:28,
              3:31,
              4:30,
              5:31,
              6:30,
              7:31,
              8:31,
              9:30,
              10:31,
              11:30,
              12:31}
    year = int(dates[0])
    if dates[0][2:] == "00":
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            months[2] = 29
    else:
        if year%4 == 0:
            months[2] = 29
    output = 0
    for i in range(int(dates[1])):
        output += months[i]
    return output + int(dates[2])


date = "2000-01-09"
date = "2019-02-10"
date = "2003-03-01"
print(dayOfYear(date))
