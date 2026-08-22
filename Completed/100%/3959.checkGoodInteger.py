# 3959. Check Good Integer
# https://leetcode.com/problems/check-good-integer/description/
# Beats: 100.00%
def checkGoodInteger(n):
    digitSum, squareSum = 0, 0
    for i in str(n):
        digitSum += int(i)
        squareSum += int(i)**2
    if squareSum - digitSum >= 50:
        return True
    return False


n  = 1000
print(checkGoodInteger(n))
