# 3745. Maximize Expression of Three Elements
# Beats: 100.00%
def maximizeExpressionOfThree(nums):
    nums = sorted(nums)
    a = nums[-1]
    b = nums[-2]
    c = nums[0]
    return a+b-c


nums = [1,4,2,5]
nums = [-2,0,5,-2,4]
print(maximizeExpressionOfThree(nums))
