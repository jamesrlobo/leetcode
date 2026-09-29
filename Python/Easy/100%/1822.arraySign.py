# 1822. Sign of the Product of an Array
# Beats: 100.00%
def arraySign(nums):
    prod = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            return 0
        prod *= (nums[i])
    if prod > 0:
        return 1
    else:
        return -1


# nums = [-1,-2,-3,-4,3,2,1]
# nums = [1,5,0,2,-3]
nums = [-1,1,-1,1,-1]
print(arraySign(nums))
