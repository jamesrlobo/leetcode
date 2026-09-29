# 3452. Sum of Good Numbers
# Beats: 46.93%
def sumOfGoodNumbers(nums):
    output = 0
    n = len(nums)
    for i in range(len(nums)):
        isboolean = True
        if i-k >= 0:
            if nums[i-k] >= nums[i]:
                isboolean = False
        if i+k < n:
            if nums[i] <= nums[i+k]:
                isboolean = False
        if isboolean == True:
            output += nums[i]
    return output


# nums = [1,3,2,1,5,4]
# k = 2
nums = [2,1]
k = 1
print(sumOfGoodNumbers(nums))
