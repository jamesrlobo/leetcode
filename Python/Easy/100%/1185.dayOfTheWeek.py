# 1185. Day of the Week
# https://leetcode.com/problems/day-of-the-week/
# Beats: 100.00%
def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    totalDays = 0
    for i in range(1970, year):
        if i%400 == 0 or (i%4 == 0 and i%100 != 0):
            totalDays += 366
        else:
            totalDays += 365
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        months[1] = 29
    for j in range(month-1):
        totalDays += (months[j])
    totalDays += day-1
    # print("Total Days:", totalDays)
    output = totalDays%7
    days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    return days[output-1]
