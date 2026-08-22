# 1716. Calculate Money in Leetcode Bank
def totalMoney(n):
    output = 0
    week = 1
    while week <= int(n/7):
        print("Week:", week)
        for i in range(week, week+7):
            output += i
        print("Weekly Sum:", output)
        week +=1
    days = int(n%7)
    print("days:",days)
    j = 1
    while j <= days:
        output += week
        week+=1
        j+=1
    return output


n = 10
# n = 20
print(totalMoney(n))
