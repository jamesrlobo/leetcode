# 3232. Find if Digit Game Can Be Won
def canAliceWin(nums):
    single_digit = [x for x in nums if x < 10]
    double_digit = [x for x in nums if x > 9]
    if sum(single_digit) == sum(double_digit):
        return False
    return True

# nums = [1,2,3,4,10]
# nums = [1,2,3,4,5,14]
nums = [5,5,5,25]
print(canAliceWin(nums))
