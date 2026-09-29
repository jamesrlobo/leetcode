# 2535. Difference Between Element Sum and Digit Sum of an Array
# Beats: 47.08%
def differenceOfSum(nums):
    elementSum, digitSum = 0, 0
    elementSum = sum(nums)
    for i in nums:
        if i > 9:
            for j in str(i):
                digitSum += int(j)
        else:
            digitSum += int(i)
    return abs(elementSum-digitSum)


nums = [1,15,6,3]
nums = [1,2,3,4]
print(differenceOfSum(nums))
