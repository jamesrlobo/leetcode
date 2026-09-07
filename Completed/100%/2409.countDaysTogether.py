# 2409. Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/description/
# Beats: 100.00%
def count_days(date):
    print(date)
    days = 0
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(int(date[0])-1):
        days += days_month[i]
    days += int(date[1])
    return days
def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    arriveAlice = arriveAlice.split("-")
    leaveAlice = leaveAlice.split("-")
    arriveBob = arriveBob.split("-")
    leaveBob = leaveBob.split("-")
    arriveAlice = count_days(arriveAlice)
    leaveAlice = count_days(leaveAlice)
    arriveBob = count_days(arriveBob)
    leaveBob = count_days(leaveBob)
    # print(arriveAlice, leaveAlice, arriveBob, leaveBob)
    return max(0, (min(leaveAlice, leaveBob)) - (max(arriveAlice, arriveBob)) + 1)


arriveAlice = "09-01"
leaveAlice = "10-19"
arriveBob = "06-19"
leaveBob = "10-20"

# arriveAlice = "08-15"
# leaveAlice = "08-18"
# arriveBob = "08-16"
# leaveBob = "08-19"

# arriveAlice = "10-01"
# leaveAlice = "10-31"
# arriveBob = "11-01"
# leaveBob = "12-31"
print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
